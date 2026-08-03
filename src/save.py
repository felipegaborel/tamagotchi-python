from pathlib import Path
import json


class SaveManager:
    def __init__(self, path: str = "save.json"):
        self.path = Path(path)

    def save(self, data: dict):
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(data, file)

    def load(self):
        if not self.path.exists():
            return None

        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)
