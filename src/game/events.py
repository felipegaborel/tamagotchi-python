class Events:
    def __init__(self, animal):
        self.animal = animal

    def pet_encontrou_comida(self):
        self.animal.energy = min(10, self.animal.energy + 20)
        self.animal._sync_attributes()
        return "Seu pet encontrou comida"

    def pet_ficou_doente(self):
        self.animal.saude = max(0, self.animal.saude - 30)
        self.animal._sync_attributes()
        return "Seu pet ficou doente"

    def pet_encontrou_brinquedo(self):
        self.animal.happiness = min(10, self.animal.happiness + 15)
        self.animal._sync_attributes()
        return "Seu pet encontrou um brinquedo"

    @staticmethod
    def get_event_texts():
        return [
            "Seu pet encontrou comida",
            "Seu pet ficou doente",
            "Seu pet encontrou um brinquedo",
        ]
