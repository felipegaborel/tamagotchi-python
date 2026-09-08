import json
import os


class SaveManager:

    SAVE_FILE = os.path.join("src", "save", "saves", "pet.json")

    @staticmethod
    def salvar(pet):

        save_dir = os.path.dirname(SaveManager.SAVE_FILE)
        os.makedirs(save_dir, exist_ok=True)

        # garante que atributos legados existam
        if hasattr(pet, "_sync_attributes"):
            pet._sync_attributes()

        dados = {
            "nome": getattr(pet, "nome", getattr(pet, "name", "")),
            "especie": pet.__class__.__name__,
            "energia": getattr(pet, "energia", getattr(pet, "energy", 0)),
            "fome": getattr(pet, "fome", getattr(pet, "hunger", 0)),
            "felicidade": getattr(pet, "felicidade", getattr(pet, "happiness", 0)),
            "saude": getattr(pet, "saude", getattr(pet, "health", 0)),
            "idade": getattr(pet, "idade", getattr(pet, "age", 0)),
            "vivo": getattr(pet, "esta_vivo", getattr(pet, "alive", False)),
            "nivel": getattr(pet, "nivel", getattr(pet, "level", 1)),
            "xp": getattr(pet, "xp", 0),
        }

        with open(SaveManager.SAVE_FILE, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print("\n💾 Jogo salvo com sucesso!")

    @staticmethod
    def carregar():

        if not os.path.exists(SaveManager.SAVE_FILE):
            return None

        with open(SaveManager.SAVE_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
