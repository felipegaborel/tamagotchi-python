import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from animals.animal import Animal


class AnimalTests(unittest.TestCase):
    def test_animal_status_contains_expected_fields(self):
        animal = Animal("Mochi")

        status = animal.status()

        self.assertEqual(status["name"], "Mochi")
        self.assertEqual(status["hunger"], 5)
        self.assertEqual(status["happiness"], 5)
        self.assertEqual(status["energy"], 5)

    def test_animal_actions_update_status(self):
        animal = Animal("Mochi")

        animal.feed()
        animal.play()
        animal.sleep()

        status = animal.status()

        self.assertEqual(status["hunger"], 6)
        self.assertEqual(status["happiness"], 6)
        self.assertEqual(status["energy"], 5)


if __name__ == "__main__":
    unittest.main()
