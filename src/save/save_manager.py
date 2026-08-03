import json
import os


class SaveManager:

    SAVE_FILE = "src/save/saves/pet.json"

    @staticmethod
    def salvar(pet):

        os.makedirs("src/save/saves", exist_ok=True)

        dados = {
            "nome": pet.nome,
            "especie": pet.especie,
            "energia": pet.energia,
            "fome": pet.fome,
            "felicidade": pet.felicidade,
            "saude": pet.saude,
            "idade": pet.idade,
            "vivo": pet.vivo,
            "nivel": pet.nivel,
            "xp": pet.xp
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
