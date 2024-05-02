# appdb_menu.py (Applied Databases project)
#
# A Python function to draw the menu of options, check the entered choice is a valid integer and returns
# the value to the main program. Range checking is done by the main program.
#
# Author: David O'Connell
#
# ***************************************************************************************************

# Define the function that will be called from the main program
def do_menu():

    choices = ('1', '2', '3', '4', '5', '6', '7', 'x')

    # The do_menu() function just draws the menu and returns the choice
    print("\n====================================")
    print("                MENU               ")
    print("====================================")
    print("1 - View Cities by Country")
    print("2 - Update City Population")
    print("3 - Add New Person")
    print("4 - Delete Person")
    print("5 - View Countries by population")
    print("6 - Show Twinned Cities")
    print("7 - Twin with Dublin")
    print("x - Exit application")

    # Check that the entered value is one of the menu options
    choice = input("Choice: ")
    if choice not in choices:
        choice = '0'
    return choice

# Test to run routine standalone
if __name__ == "__main__":
    do_menu()