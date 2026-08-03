class AchievementSystem:

    @staticmethod
    def verificar(pet):

        conquistas = []

        if pet.idade >= 10:
            conquistas.append("🐣 Primeiro Crescimento")

        if pet.nivel >= 5:
            conquistas.append("⭐ Pet Experiente")

        if pet.felicidade == 100:
            conquistas.append("😊 Muito Feliz")

        if pet.saude == 100:
            conquistas.append("❤️ Saúde de Ferro")

        return conquistas
