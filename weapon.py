from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def name(self) -> str:
        pass

class Sword(Weapon):
    def action(self):
        print("You wield your sword and attack your opponent.")

    def name(self):
        return "a sharp sword"

class Bow(Weapon):
    def __init__(self):
        self.arrows = 3

    def action(self):
        if self.arrows > 0:
            print("You hold your breath and shoot an arrow at your opponent.")
            self.arrows = self.arrows - 1
            print(f"You have {self.arrows} arrows left.")
        else:
            print("You're out of arrows.")

    def name(self):
        return "a fine set of bow and arrows"

class Wand(Weapon):
    def __init__(self):
        self.casting = False

    def action(self):
        if self.casting:
            print("You throw a fireball at your opponent's face.")
            self.casting = False
        else:
            print("You are casting.")
            self.casting = True

    def name(self):
        return "an ancient wand"
