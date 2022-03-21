print("Welcome to PSB Battle Game! \n(N)ew game\n(S)ave game\n(Q)uit!")


def main():
    selection = input("Choose your option then hit <ENTER> ==> ")
    if selection.upper() == "N":
        new_game()
    elif selection.upper() == "S":
        print("Loading save game...")
        pass
    elif selection.upper() == "Q":
        print("Exit game...")
        pass
    else:
        print("I don't understand what are you typing.")
        return main()


def new_game():
    print("\nSetting up Player 1 team...\n")
    name_list = []
    for unit_name in range(1, 4):
        print("Enter a unique name for unit #{unit_name}-> ", end="")
        name = input("")
        repeated = False
        while repeated:
            if name == "":
                continue
        repeated = True
        if name in name_list:
            print("\nUnit name must be unique.\n")
            return new_game()
        if not name.strip():
            print("\nUnit name could not be blank.\n")
            return new_game()
        else:
            print("Name looks good!")
            name_list.append(name)
            print(
                f"Select unit #{unit_name}, type: (W)arrior, (T)anker, or Wi(Z)ard ==> ",
                end="",
            )
            role = input("")
            if role.upper() == "W":
                print("Added " + str(name_list))
                warrior()
            elif role.upper() == "T":
                print("Added " + str(name_list))
                tanker()
            elif role.upper() == "Z":
                print("Added " + str(name_list))
                wizard()
            else:
                print("I don't understand what are you typing.")
                return role()


def warrior():
    charac = [1, 50, 8, 3, 0, "True", "False", "False"]
    print(
        "\nWarrior Level 1: ",
        "HP =",
        charac[1],
        "," "ATK =",
        charac[2],
        "," "DEF =",
        charac[3],
        "," "EXP =",
        charac[4],
        "," "ALIVE =",
        charac[5],
        "," "POISONED =",
        charac[6],
        "," "FROZEN =",
        charac[7],
    )
    print()


def tanker():
    charac = [1, 60, 5, 5, 0, "True", "False", "False"]
    print(
        "\nTanker Level 1: ",
        "HP =",
        charac[1],
        "," "ATK =",
        charac[2],
        "," "DEF =",
        charac[3],
        "," "EXP =",
        charac[4],
        "," "ALIVE =",
        charac[5],
        "," "POISONED =",
        charac[6],
        "," "FROZEN =",
        charac[7],
    )
    print()


def wizard():
    charac = [1, 40, 3, 2, 0, "True", "False", "False"]
    print(
        "\nWizard Level 1: ",
        "HP =",
        charac[1],
        "," "ATK =",
        charac[2],
        "," "DEF =",
        charac[3],
        "," "EXP =",
        charac[4],
        "," "ALIVE =",
        charac[5],
        "," "POISONED =",
        charac[6],
        "," "FROZEN =",
        charac[7],
    )
    print()


main()
