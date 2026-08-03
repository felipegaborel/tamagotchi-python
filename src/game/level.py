class LevelSystem:

    @staticmethod
    def ganhar_xp(pet, quantidade):

        pet.xp += quantidade

        while pet.xp >= 100:

            pet.xp -= 100

            pet.nivel += 1

            print(f"\n⭐ {pet.nome} subiu para o nível {pet.nivel}!")

            pet.saude = min(100, pet.saude + 10)
