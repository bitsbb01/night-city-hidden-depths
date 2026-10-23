import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_content import validate_location


class QuietTrackContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "content" / "locations" / "quiet-track.json"
        cls.definition = json.loads(path.read_text(encoding="utf-8"))

    def test_first_location_satisfies_content_constraints(self):
        self.assertEqual(validate_location(self.definition), [])

    def test_hostage_chance_must_remain_five_percent(self):
        changed = copy.deepcopy(self.definition)
        changed["quest"]["hostage_event_chance"] = 0.5
        errors = validate_location(changed)
        self.assertTrue(any("0.05 (5%)" in error for error in errors))

    def test_playtime_must_reach_twenty_minutes(self):
        changed = copy.deepcopy(self.definition)
        changed["target_playtime_minutes"] = 19
        errors = validate_location(changed)
        self.assertTrue(any("at least 20 minutes" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
