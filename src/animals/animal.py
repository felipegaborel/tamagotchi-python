from dataclasses import dataclass, field
from typing import Dict, List

from game.achievements import AchievementSystem

MAX_VALUE = 100
MIN_VALUE = 0
BAR_WIDTH = 20


# Observação de design:
# Este módulo define atributos canônicos em inglês (name, age, health, hunger, happiness, energy).
# Para compatibilidade retroativa com código em português, _sync_attributes() cria aliases PT-BR
# (nome, idade, saude, fome, felicidade, energia, nivel, esta_vivo). As alterações no projeto
# migraram a maioria do código para usar os atributos canônicos enquanto mantêm os aliases.

@dataclass
class Animal:
    # Core (English) attributes
    name: str
    age: int = 0
    health: int = field(default=100)
    hunger: int = field(default=50)
    happiness: int = field(default=50)
    energy: int = field(default=50)
    level: int = field(default=1)
    xp: int = field(default=0)
    alive: bool = field(default=True)

    def __post_init__(self) -> None:
        # Ensure PT-BR aliases exist and are synchronized
        self._sync_attributes()

    def _clamp(self, value: int) -> int:
        return max(MIN_VALUE, min(MAX_VALUE, int(value)))

    def _sync_attributes(self) -> None:
        # Portuguese aliases (kept for compatibility)
        self.nome = self.name
        self.idade = self.age
        self.saude = self.health
        self.fome = self.hunger
        self.felicidade = self.happiness
        self.energia = self.energy
        self.nivel = self.level
        self.esta_vivo = self.alive

    # Core actions (English)
    def feed(self, amount: int = 10) -> None:
        self.hunger = self._clamp(self.hunger - amount)
        self._sync_attributes()

    def play(self, energy_cost: int = 10, happiness_gain: int = 15, hunger_increase: int = 10) -> None:
        self.energy = self._clamp(self.energy - energy_cost)
        self.happiness = self._clamp(self.happiness + happiness_gain)
        self.hunger = self._clamp(self.hunger + hunger_increase)
        self._sync_attributes()

    def sleep(self, energy_gain: int = 30, hunger_increase: int = 15) -> None:
        self.energy = self._clamp(self.energy + energy_gain)
        self.hunger = self._clamp(self.hunger + hunger_increase)
        self._sync_attributes()

    def bath(self, happiness_gain: int = 5) -> None:
        self.happiness = self._clamp(self.happiness + happiness_gain)
        self._sync_attributes()

    # Compatibility (Portuguese) aliases — call the English methods
    def alimentar(self, amount: int = 10) -> None:
        self.feed(amount)

    def brincar(self) -> None:
        # Keep legacy signature (no args)
        self.play()

    def dormir(self) -> None:
        self.sleep()

    def banho(self) -> None:
        self.bath()

    # Status helpers
    def status(self) -> Dict:
        """Return a dict with both English and Portuguese keys (backwards compat)."""
        self._sync_attributes()
        return {
            "name": self.name,
            "nome": self.nome,
            "age": self.age,
            "idade": self.idade,
            "health": self.health,
            "saude": self.saude,
            "hunger": self.hunger,
            "fome": self.fome,
            "happiness": self.happiness,
            "felicidade": self.felicidade,
            "energy": self.energy,
            "energia": self.energia,
            "level": self.level,
            "nivel": self.nivel,
            "xp": self.xp,
            "alive": self.alive,
            "esta_vivo": self.esta_vivo,
        }

    def status_bar(self, value: int, width: int = BAR_WIDTH) -> str:
        v = self._clamp(value)
        filled = int((v / MAX_VALUE) * width)
        return "█" * filled + "░" * (width - filled)

    # Keep mostrar_status for UI compatibility (prints formatted status)
    def mostrar_status(self) -> None:
        self._sync_attributes()
        print("\n" + "=" * 50)
        print(f"🐶 {self.nome}")
        print()
        print(f"❤️ Saúde      {self.status_bar(self.health)} {self.health}")
        print(f"⚡ Energia    {self.status_bar(self.energy)} {self.energy}")
        print(f"🍖 Fome       {self.status_bar(self.hunger)} {self.hunger}")
        print(f"😊 Felicidade {self.status_bar(self.happiness)} {self.happiness}")
        print(f"⭐ Nível: {self.level}")
        print(f"✨ XP: {self.xp}/100")
        print("\n🏆 Conquistas")
        # AchievementSystem is kept; verificar() should accept an Animal instance
        for conquista in AchievementSystem.verificar(self):
            print(conquista)
        print("=" * 50)