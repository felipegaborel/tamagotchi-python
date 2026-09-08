class Events:
    def __init__(self, animal):
        self.animal = animal

    # Observações:
    # - Eventos agora atualizam atributos canônicos (energy/health/happiness) e chamam _sync_attributes()
    #   para manter compatibilidade com código legado que usa atributos em português.

    def pet_encontrou_comida(self):
        # aumenta energia (até 100)
        self.animal.energy = min(100, self.animal.energy + 20)
        self.animal._sync_attributes()
        return "Seu pet encontrou comida"

    def pet_ficou_doente(self):
        # diminui saúde
        self.animal.health = max(0, self.animal.health - 30)
        self.animal._sync_attributes()
        return "Seu pet ficou doente"

    def pet_encontrou_brinquedo(self):
        # aumenta felicidade
        self.animal.happiness = min(100, self.animal.happiness + 15)
        self.animal._sync_attributes()
        return "Seu pet encontrou um brinquedo"

    @staticmethod
    def get_event_texts():
        return [
            "Seu pet encontrou comida",
            "Seu pet ficou doente",
            "Seu pet encontrou um brinquedo",
        ]
