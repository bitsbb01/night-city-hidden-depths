-- Night City Hidden Depths - CET test scaffold
-- Install this folder under:
-- bin/x64/plugins/cyber_engine_tweaks/mods/night_city_hidden_depths/

local Encounter = require("door_encounter")
local json = require("json")

local MOD_NAME = "Night City Hidden Depths"
local STATE_FILE = "progress.json"

local function newState()
  return {
    Nette_Rescued = false,
    Josiah_Rescued = false,
    Arcade_Owner_Rescued = false,
    rescued = {},
    usedDoors = {},
    crates = {},
    turretsPowered = { false, false, false, false },
  }
end

local state = newState()

local function loadState()
  local file = io.open(STATE_FILE, "r")
  if not file then
    return
  end

  local contents = file:read("*a")
  file:close()

  if not contents or contents == "" then
    return
  end

  local ok, decoded = pcall(json.decode, contents)
  if not ok or type(decoded) ~= "table" then
    print("[NCHD] progress.json could not be decoded; starting with defaults")
    return
  end

  local defaults = newState()
  for key, value in pairs(defaults) do
    if decoded[key] == nil then
      decoded[key] = value
    end
  end
  decoded.rescued = decoded.rescued or {}
  decoded.usedDoors = decoded.usedDoors or {}
  decoded.crates = decoded.crates or {}
  decoded.turretsPowered = decoded.turretsPowered or { false, false, false, false }
  state = decoded
end

local function saveState()
  local file, err = io.open(STATE_FILE, "w")
  if not file then
    print("[NCHD] Could not save progress.json: " .. tostring(err))
    return false
  end

  local ok, encoded = pcall(json.encode, state)
  if not ok then
    file:close()
    print("[NCHD] Could not encode progress state: " .. tostring(encoded))
    return false
  end

  file:write(encoded)
  file:close()
  return true
end

local function doorKey(door)
  local position = door:GetWorldPosition()
  return string.format("%.1f:%.1f:%.1f", position.x, position.y, position.z)
end

local function getLookedAtDoor()
  local player = Game.GetPlayer()
  if not player then
    return nil, "Player is not available yet"
  end

  local target = Game.GetTargetingSystem():GetLookAtObject(player, false, false)
  if not target then
    return nil, "Aim at a real door first"
  end

  local typeName = tostring(target:ToString())
  if typeName ~= "Door" then
    return nil, "Target is " .. typeName .. "; aim at a real door"
  end

  return target
end

local function forceOpenDoor(door)
  local devicePS = door:GetDevicePS()
  if devicePS then
    if devicePS:IsSealed() then
      devicePS:ToggleSealOnDoor()
    end
    if devicePS:IsLocked() then
      devicePS:ToggleLockOnDoor()
    end
  end
  door:OpenDoor()
end

local function printEncounter(encounter)
  print("[NCHD] Door encounter: " .. tostring(encounter.category))

  if encounter.category == "Random_Dungeon" then
    print("[NCHD] Archetype=" .. tostring(encounter.archetype)
      .. " | enemy pool=" .. tostring(encounter.enemyPool)
      .. " | scenario=" .. tostring(encounter.scenario))
    if encounter.hostageKey then
      print("[NCHD] Hostage selected: " .. tostring(encounter.hostageKey)
        .. " (ID " .. tostring(encounter.hostageId) .. ")")
    end
  elseif encounter.category == "Ambient_Room" then
    print("[NCHD] Ambient scene=" .. tostring(encounter.scene))
  elseif encounter.category == "Stash_Room" then
    print("[NCHD] Stash table=" .. tostring(encounter.lootTable))
  end

  print("[NCHD] Selection only: this scaffold does not yet spawn room geometry, NPCs, or loot.")
end

local function rollTargetDoor()
  local door, reason = getLookedAtDoor()
  if not door then
    print("[NCHD] " .. reason)
    return
  end

  local key = doorKey(door)
  if state.usedDoors[key] then
    print("[NCHD] This door has already rolled in this persistent progress file.")
    return
  end

  -- Mark before opening so a failed animation does not reroll the same door.
  state.usedDoors[key] = true
  local encounter = Encounter.Roll(state)
  saveState()

  local ok, err = pcall(forceOpenDoor, door)
  if not ok then
    print("[NCHD] Door roll saved, but CET could not open this target: " .. tostring(err))
    printEncounter(encounter)
    return
  end

  printEncounter(encounter)
end

local function markHostageRescued(hostageKey)
  state = Encounter.MarkHostageRescued(state, hostageKey)
  saveState()
  print("[NCHD] Rescue state saved: " .. hostageKey)
end

registerForEvent("onInit", function()
  loadState()
  print("[NCHD] " .. MOD_NAME .. " loaded. Progress file: " .. STATE_FILE)
end)

-- CET requires users to bind their own keys in the overlay.
registerHotkey("nchd_roll_target_door", "NCHD: Open aimed door and roll encounter", rollTargetDoor)
registerHotkey("nchd_test_roll_only", "NCHD: Test encounter roll (no door)", function()
  local encounter = Encounter.Roll(state)
  printEncounter(encounter)
end)
registerHotkey("nchd_rescue_nette_test", "NCHD: Test mark Nette rescued", function()
  markHostageRescued("Nette")
end)
registerHotkey("nchd_rescue_josiah_test", "NCHD: Test mark Josiah rescued", function()
  markHostageRescued("Josiah")
end)
registerHotkey("nchd_rescue_arcade_test", "NCHD: Test mark Arcade Owner rescued", function()
  markHostageRescued("Arcade_Owner")
end)
