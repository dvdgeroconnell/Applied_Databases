

# Define the imports here
import appdb_menu as apm
import cities_by_country as cbc
import city_population as cp

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
                print("3...")

            case '4':
                print("4...")

            case '5':
                print("5...")

            case '6':
                print("6...")

            case '7':
                print("6...")

            case _:
                # Catch-all for entries other than the ones listed above
                print("Invalid entry, exiting...")
                run = False

if __name__=="__main__":
    main()
