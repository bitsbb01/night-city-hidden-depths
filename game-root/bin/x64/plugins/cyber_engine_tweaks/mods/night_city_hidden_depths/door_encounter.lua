-- Night City Hidden Depths: door encounter selection
-- Pure selection logic for a CET mod. Connect the returned encounter config
-- to the game's door, NPC, loot, and dungeon spawning hooks separately.

local DoorEncounter = {}

DoorEncounter.DungeonArchetypes = {
  "Badlands_Bunker",
  "NC_Sewer_System",
  "Corp_Sub_Level",
  "Abandoned_Metro",
  "Utility_Vault",
  "Abandoned_Train_Station",
  "Subterranean_Transit_Hub",
  "Deep_Maintenance_Depot",
}

-- Replace these labels with the exact CET/game gang identifiers once the
-- enemy spawner is wired in. Keep this pool to gangs available in the world.
DoorEncounter.EnemyPools = {
  "Maelstrom",
  "Tyger_Claws",
  "Valentinos",
  "6th_Street",
  "Animals",
  "Scavengers",
  "Wraiths",
}

DoorEncounter.Hostages = {
  { id = 1, key = "Nette" },
  { id = 2, key = "Josiah" },
  { id = 3, key = "Arcade_Owner" },
}

-- Equal odds within the 65% ambient-room result.
DoorEncounter.AmbientScenes = {
  "Empty_Room",
  "NPC_Using_Drugs",
  "Consensual_Adult_Encounter",
}

local function choose(list)
  return list[math.random(1, #list)]
end

local function rescued(state, hostageKey)
  if not state then
    return false
  end
  local jsonKey = hostageKey .. "_Rescued"
  return (state.rescued and state.rescued[hostageKey] == true)
    or state[jsonKey] == true
end

local function chooseUnrescuedHostage(state)
  local available = {}
  for _, hostage in ipairs(DoorEncounter.Hostages) do
    if not rescued(state, hostage.key) then
      available[#available + 1] = hostage
    end
  end

  if #available == 0 then
    return nil
  end
  return choose(available)
end

-- One call per successfully unlocked/opened eligible door.
-- Exact top-level odds: 1-25 dungeon, 26-90 ambient, 91-100 stash.
function DoorEncounter.Roll(state)
  local roll = math.random(1, 100)

  if roll <= 25 then
    local encounter = {
      category = "Random_Dungeon",
      archetype = choose(DoorEncounter.DungeonArchetypes),
      enemyPool = choose(DoorEncounter.EnemyPools),
      roll = roll,
    }

    -- Hostages are a 5% secondary roll inside the dungeon branch.
    encounter.hostageRoll = math.random(1, 100)
    if encounter.hostageRoll <= 5 then
      local hostage = chooseUnrescuedHostage(state)
      if hostage then
        encounter.scenario = "Hostage_Rescue"
        encounter.hostageId = hostage.id
        encounter.hostageKey = hostage.key
      else
        encounter.scenario = "Standard_Clear"
      end
    else
      encounter.scenario = "Standard_Clear"
    end

    return encounter
  end

  if roll <= 90 then
    return {
      category = "Ambient_Room",
      scene = choose(DoorEncounter.AmbientScenes),
      roll = roll,
    }
  end

  return {
    category = "Stash_Room",
    lootTable = "Weapons_Food_Consumables_Cyberware",
    roll = roll,
  }
end

-- Call only after the rescue interaction has actually completed.
function DoorEncounter.MarkHostageRescued(state, hostageKey)
  if not state then
    state = {}
  end
  state.rescued = state.rescued or {}

  for _, hostage in ipairs(DoorEncounter.Hostages) do
    if hostage.key == hostageKey then
      state.rescued[hostageKey] = true
      state[hostageKey .. "_Rescued"] = true
      return state
    end
  end

  return state, "unknown_hostage"
end

return DoorEncounter
