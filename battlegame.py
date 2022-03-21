wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    option = input("Choose your character: ")
    if option == "1":
        character = wizard
        my_damage = wizard_damage
        my_hp = wizard_hp
        break
    elif option == "2":
        character = elf
        my_damage = elf_damage
        my_hp = elf_hp
        break
    elif option == "3":
        character = human
        my_damage = human_damage
        my_hp = human_hp
        break
print("You have chosen the:", character)
print("Health:", my_hp)
print("Damage:", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hp are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - damage_hp
    print("The Dragon strikes back at", character)
    print("The", character, "hp are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
