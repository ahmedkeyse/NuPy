def main():
    # define variables
    # ask for user input, enumerate list, provide list for user and change input from str to int
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"
    end_game = "End Game"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 200
    orc_hp = 90
    dragon_hp = 300

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 105
    dragon_damage = 50

    character_list = [wizard, elf, human, orc, end_game]

    for i, value in enumerate(character_list, 1):
        print("{}.) {}".format(i, value))

    character = int(input("\nSelect A Number To Choose Your Character:"))

    while True:
        # ask plater to choose character and give stats of character.
        # if unknown character is entered continue loop.
        # give player an option to end game.
        # character = (int(input("\nSelect A Number To Choose Your Character:")))
        if character == 1:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == 2:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == 3:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        # bonus 3 - add an additional character with hp and damage
        elif character == 4:
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        # bonus 4 - give player the option to not continue playing the game and exit program.
        elif character == 5:
            print("\nDid you forget your sword? Maybe next time.\n")
            quit()
        print("Unknown Character")

    print(f"\nYou have chosen the character: ", character)
    print("Health:", my_hp)
    print("Damage:", my_damage)

    while True:
        # provide results of battle with dragon based on player choice
        # and initialized global variables
        dragon_hp = dragon_hp - my_damage
        print(f"\nThe {character} damaged the Dragon!")
        if dragon_hp > 0:
            print(f"The dragon has {dragon_hp}left.\n")
        elif dragon_hp <= 0:
            print(f"The Dragon has lost the battle. {character} wins!\n")
            break
        my_hp = my_hp - dragon_damage
        print(f"\nThe Dragon damaged the {character}! You have {my_hp} left!\n")
        elif my_hp <= 0:
            print(f"The has lost the battle.\n")
            break
    # bonus 5 ask user if they would like to play again once
    # winner is determined
    again = input("Would you like to play again? Type yes or no. :")
    # made str input case insensitive
    if again.casefold() == "yes":
        main()
    else:
        quit()


main()
