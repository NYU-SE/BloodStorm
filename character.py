from abc import ABC, abstractmethod
from weapon import Weapon

class State(ABC):
    def __init__(self, character: "Character"):
        self.character = character

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def heal(self):
        pass

    @abstractmethod
    def takeDamage(self):
        pass

class HealthyState(State):
    def attack(self):
        print("Attack at your peak performance!")
        self.character.weapon.action()

    def heal(self):
        print("You are healthy, no need to heal.")

    def takeDamage(self):
        print("You've been injured!")
        self.character.changeState(SurvivingState(self.character))

class SurvivingState(State):
    def attack(self):
        print("Attack despite the pain.")
        self.character.weapon.action()

    def heal(self):
        print("You recover from the pain.")
        self.character.changeState(HealthyState(self.character))

    def takeDamage(self):
        print("You've been defeated!")
        self.character.changeState(DefeatedState(self.character))

class DefeatedState(State):
    def attack(self):
        print("You can't even lift a finger.")

    def heal(self):
        print("Too late.")

    def takeDamage(self):
        print("Your opponent is very ungraceful.")

class Character:
    def __init__(self, initial_weapon: Weapon):
        self.state = HealthyState(self)
        self.weapon = initial_weapon
    
    def attack(self):
        self.state.attack()

    def heal(self):
        self.state.heal()

    def takeDamage(self):
        self.state.takeDamage()

    def changeState(self, state: State):
        self.state = state

    def equip(self, weapon: Weapon):
        self.weapon = weapon
        print(f"You equip {weapon.name()}")
