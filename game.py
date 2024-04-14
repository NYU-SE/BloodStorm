from character import Character
from weapon import Sword, Bow, Wand

print("Game start.")

character = Character(Sword())
while True:
    action = input("Your action: ")
    match action.split():
        case ["attack"]:
            character.attack()
        case ["heal"]:
            character.heal()
        case ["end","turn"]:
            print("Your opponent attacks!")
            character.takeDamage()
        case ["equip", weapon]:
            match weapon:
                case "sword":
                    character.equip(Sword())
                case "bow":
                    character.equip(Bow())
                case "wand":
                    character.equip(Wand())
                case other_weapon:
                    print(f"{other_weapon} is currently not available in the shop.")
        case ["restart"]:
            character = Character(Sword())
            print("Gamae restarted.")
        case ["exit"]:
            print("Bye!")
            break
        case _:
            print("Did not recognize this command.")
