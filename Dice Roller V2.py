# Basic Dice Rolling program
# V2 Adds title, modularity and BASIC Macro support

from os import remove
from random import randint


# Roll some dice
def roll_func(dice, size, mod):
    if dice < 1:
        print("You need to roll at least one die.")
        dice = 1

    if size < 2:
        print("Dice need at least 2 sides.")
        size = 2
    
    total_roll = 0
    for x in range(dice):
        die = randint(1, size)
        total_roll += die
        print(die)
    print("Total:", total_roll + mod, "\n")


def manual_roller():
    rolling = True
    while rolling:
        # Get number of dice to roll, minimum 1
        try:
            dice_to_roll = int(input("Number of dice to roll: "))
        except ValueError:
            print("That's not a number! Rolling one die instead.")
            dice_to_roll = 1
        
        # Get number of sides for dice
        try:
            dice_size = int(input("Size of dice to roll: "))
        except ValueError:
            print("Dice need at least 2 sides.")
            dice_size = 2

        # Get dice modifier
        try:
            dice_modifier = int(input("Dice modifier +/-: "))
        except TypeError:
            dice_modifier = 0
        except ValueError:
            dice_modifier = 0

        roll_func(dice_to_roll, dice_size, dice_modifier)
        if input("Roll again, or return to Main? ") == "Main":
            rolling = False


def macro_roller():
    # Ensure Macro file exists. Create one if it doesn't
    try:
        open("DiceRollerMacros.txt", "x")
    except FileExistsError:
        print("Macro file found!")
    else:
        with open("DiceRollerMacros.txt") as macro_file:
            macro_file.write("000 000 000 || DICE/SIDES/MODIFIER || Comments ||||")
        print("No macro file found. Macro file created.")

    run_macro = True
    while run_macro:
        macro_func = input("Would you like to Read, Write or Purge macros, or return to the Main menu? ")
        if macro_func == "Main":
            run_macro = False

        # Open the file in READ mode
        elif macro_func == "Read":
            # Open the macro file and print out everything for ease of user selection
            with open("DiceRollerMacros.txt", "r") as macro_file:
                print("Please select a macro from the list using the number at the beginning: ")
                line_num = 0
                for i in open("DiceRollerMacros.txt", "r"):
                    print("#", line_num, "", macro_file.readline())
                    line_num += 1

            # Open the macro file again, grab user selection, format, and feed into roll_func()
            with open("DiceRollerMacros.txt", "r") as macro_file:
                macro_line = macro_file.readlines()
                macro_line_select = (macro_line[int(input("Which Macro line would you like to Execute? "))])
                roll_func(int(macro_line_select[0:3]), int(macro_line_select[4:7]), int(macro_line_select[8:11]))

        # Open the file in WRITE mode
        elif macro_func == "Write":
            with open("DiceRollerMacros.txt", "a") as macro_file:
                print("Macros are written with the following Dice/Size/Mod syntax.\n"
                      "Failure to obey write rules will break program, but any comments may be added after.\n"
                      " D   S   M\n"
                      "000 000 000")
                macro_file.write(input("Please type macro to be written on line below:\n"))

        # Delete existing macro file and create new blank file
        elif macro_func == "Purge":
            remove("DiceRollerMacros.txt")
            with open("DiceRollerMacros.txt", "x") as macro_file:
                macro_file.write("000 000 000 #### FORMATTING LINE ####")

        else:
            print("Invalid Option")


def main():
    print("#############################\n"
          "## Basic Bitch Dice Roller ##\n"
          "##      With  Macros!      ##\n"
          "#############################")
    while True:
        mor = input("Macro or Roller? ")
        if mor == "Macro":
            macro_roller()
        elif mor == "Roller":
            manual_roller()
        else:
            print("Option invalid!")


# if __name__ == "__Dice Roller V2.py__":
main()
