# appbd_main.py (Applied Databases project)
#
# The main Python program to present the user with a menu of options to read data from and write data to
# the appdbproj database in MySQL.
# Most of the functionality is implemented in functions contained in separate files for maintainability.
# These are imported at the top of the file below.
# 
# Author: David O'Connell
#
# ***************************************************************************************************

# Define the imports here
import appdb_menu as apm
import cities_by_country as cbc
import city_population as cp
import add_person as ap
import delete_person as dp
import country_pop as cpl
import twinned_cities as tc
import create_twin as ct

def main():

    run = True
    while (run):
        choice = apm.do_menu()
        match choice:

            case 'x':
                print("Exiting...")
                run = False

            case '0':
                # Just let the menu display again, per specification
                pass

            case '1':
                choice = input("\nEnter Country : ")
                cbc.cities_by_country(choice)

            case '2':
                result = False
                while not result:
                    choice = input("\nEnter City ID : ")
                    if choice.isdigit():
                        result = cp.city_population(choice)
                    else:
                        print("Not a valid City ID")

            case '3':
                print("Add New Person")
                print("---------------")
                # ID is a primary key, but not auto-incremented
                id = input("ID : ")
                name = input("Name : ")
                age = input("Age : ")
                salary = input("Salary : ")
                city = input("City : ")
                ap.add_person(id, name, age, salary, city)

            case '4':
                success = False
                delete_id = input("Enter ID of Person to Delete : ")
                success = dp.delete_person(delete_id)
                if success:
                    print("Person ID:", delete_id, "deleted")
                # Error handling will be done in the function

            case '5':
                # Loop until the user enters one of <, >, =, and a valid integer population
                proceed = False
                gle_options = ('<','>','=')
                print("Countries by Pop")
                print("----------------")

                while not proceed:
                    gle = input("Enter < > or = : ")
                    if gle in gle_options:
                        proceed = True

                proceed = False

                while not proceed:
                    pop = input("Enter population : ")
                    if pop.isdigit():
                        proceed = True

                cpl.country_pop(gle, pop)

            case '6':
                tc.twinned_cities()

            case '7':
                # Loop until the user enters an integer
                proceed = False
                while not proceed:
                    twin = input("Enter ID of City to twin with Dublin: ")
                    if twin.isdigit():
                        proceed = True
                ct.create_twin(twin)

            case _:
                # Catch-all for entries other than the ones listed above
                print("Invalid entry, exiting...")
                run = False

if __name__=="__main__":
    main()
