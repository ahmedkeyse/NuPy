import sys

wizard = "Wizard"
wizard_hp = 70
wizard_attack = 150
elf = "Elf"
elf_hp = 1000
elf_attack = 100
human = "Human"
human_hp = 150
human_attack = 50
dragon_hp = 300
dragon_attack = 50
# my_hp =0
# my_attack = 0
while True:
    print("1)  ", wizard)
    print("2)  ", elf)
    print("3)  ", human)
    print("4)   exit")
    character = input("Choose your character ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_attack = wizard_attack
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_attack = elf_attack
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_attack = human_attack
        break
    if character == "4":
        sys.exit()
print("Unknown Character")
print("You have chosen ", character, ":")
print("-Attack", my_attack)
print("-Health", my_hp)
while True:
    dragon_hp = 300
    dragon_hp = dragon_hp - my_attack
    print("The ", character, "damaged the Dragon!")
    print("The Dragons health is now", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    my_hp = my_hp - dragon_attack
    print("The Dragon has damaged the", character)
    print("The", character, " is now at", my_hp, "health")
    if my_hp <= 0:
        print("the ", character, "Lost the battle!")
        break
    restart = input("Would you like to battle again?")
    if restart == "yes" or "y":
        continue
