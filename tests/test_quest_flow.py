import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_quest_flow import validate_quest_flow


class QuietTrackQuestFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "content" / "quests" / "quiet-track-flow.json"
        cls.definition = json.loads(path.read_text(encoding="utf-8"))

    def test_quiet_track_quest_flow_is_valid(self):
        self.assertEqual(validate_quest_flow(self.definition), [])

    def test_flow_rejects_missing_transition_target(self):
        changed = copy.deepcopy(self.definition)
        changed["nodes"][0]["next"] = ["missing_node"]
        errors = validate_quest_flow(changed)
        self.assertTrue(any("points to missing node" in error for error in errors))

    def test_flow_rejects_unreachable_node(self):
        changed = copy.deepcopy(self.definition)
        changed["nodes"].append({
            "id": "orphan",
            "type": "objective",
            "required": False,
            "summary": "An unreachable node.",
            "next": []
        })
        errors = validate_quest_flow(changed)
        self.assertTrue(any("all quest nodes must be reachable" in error for error in errors))

    def test_flow_rejects_duplicate_save_facts(self):
        changed = copy.deepcopy(self.definition)
        changed["save_facts"].append(changed["save_facts"][0])
        errors = validate_quest_flow(changed)
        self.assertTrue(any("save facts must be unique" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
