class LevelSystem:

    @staticmethod
    def ganhar_xp(pet, quantidade):
        # garante que aliases estejam sincronizados
        if hasattr(pet, "_sync_attributes"):
            pet._sync_attributes()

        pet.xp += quantidade

        while pet.xp >= 100:
            pet.xp -= 100
            pet.level += 1
            # report using canonical names
            print(f"\n⭐ {getattr(pet, 'name', getattr(pet, 'nome', 'Pet'))} subiu para o nível {pet.level}!")
            pet.health = min(100, pet.health + 10)
            if hasattr(pet, "_sync_attributes"):
                pet._sync_attributes()
