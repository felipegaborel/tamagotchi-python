import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from animals.animal import Animal as Tamagotchi


class TamagotchiTests(unittest.TestCase):
    def test_pet_starts_with_expected_stats(self):
        pet = Tamagotchi("Mochi")

        self.assertEqual(pet.name, "Mochi")
        self.assertEqual(pet.hunger, 5)
        self.assertEqual(pet.happiness, 5)
        self.assertEqual(pet.energy, 5)

    def test_feed_and_play_change_stats(self):
        pet = Tamagotchi("Mochi")

        pet.feed()
        pet.play()

        self.assertEqual(pet.hunger, 6)
        self.assertEqual(pet.happiness, 6)
        self.assertEqual(pet.energy, 4)


if __name__ == "__main__":
    unittest.main()
