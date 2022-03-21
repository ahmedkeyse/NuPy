wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 700
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
damaage_hp = 50
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    option = input("Choose your character: ")
    if option == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if option == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if option == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("unknown character")
print(character)
print(my_hp)
print(my_damage)

while True:
    dragon_damage = dragon_damage - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hp are now:" + str(dragon_damage))
    if dragon_hp <= 0:
        print("thE Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The", character, "strikes back at the:", character)
    print("The", character, "hp are now:", my_hp)
    print("")
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
