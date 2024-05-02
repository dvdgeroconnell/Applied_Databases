
import pymysql as pml

def city_population(id):

    choices = ('I','i','D','d')

    # Use DictCursor as it is easier to get access to the attributes if the row
    db_conn = pml.connect(host="localhost", user="root", password="", db="appdbproj",
                     cursorclass=pml.cursors.DictCursor)

    sql = "SELECT ID, Name, CountryCode, Population, latitude, longitude \
           from city where ID = %s"
    
# Note - 'with' takes care of closing the connection when we are finished with it
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(sql, (id))
        # We can use fetchone() because ID is a primary key so we will get one (or no) response
        result = cursor.fetchone()
        if not result:
            print("No city found with ID = ", id)
            found = False
        else:
            print("")
            current_pop = int(result['Population'])
            for x in result:
                print(result[x], "| ", end='')
            print("\b\b  ")

            do_update = False
            choice = ''
            while choice not in choices:
                choice = input ("\n[I]ncrease\[D]ecrease Population: ")

            if choice in choices[0:2]:
                valid = False
                while not valid:
                    change = input("Enter Population Increase: ")

                    if change.isdigit():
                        print("Increasing the population by", change)
                        change = int(change) + current_pop
                        valid = True
                        do_update = True
                    else:
                        print("Enter a valid number.")
            else:
                valid = False
                while not valid:
                    change = input("Enter Population Decrease: ")
                    if change.isdigit():
                        if current_pop - int(change) >= 0:
                            print("Decreasing the population by", change)
                            change = current_pop - int(change)
                            valid = True
                        else:
                            print("That decrease is greater than the current population.")
                            # check if the decrease is greater than the population and loop if it is
                do_update=True

            if do_update:
                # Need to open the connection again...
                db_conn = pml.connect(host="localhost", user="root", password="", db="appdbproj",
                                      cursorclass=pml.cursors.DictCursor)
                
                update_sql = "UPDATE city SET Population = %s WHERE ID = %s"
                with db_conn:
                    try:
                        cursor1 = db_conn.cursor()
                        cursor1.execute(update_sql, (change, id))
                        db_conn.commit()
                    except:
                        print("ERROR - unable to complete database update.")

            found = True
    return found

# Print 2 results at a time and allow the user to quit after each 2 records by entering 'q'
'''
    count = 0
    cont = True
    while (num>0 and cont):
        for x in results[count]:
            print(results[count][x], "| ", end='')
        print("\b\b  ")
        count +=1
        num -= 1
        if (count % 2) == 0:
            choice = input("-- Quit (q) --")
            if choice == 'q':
                cont = False
    if cont == True:
        choice = input("All printed - press Enter to return to menu")
    return
'''