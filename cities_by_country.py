
import pymysql as pml

def cities_by_country(country):

    # Use DictCursor as it is easier to get access to the attributes if the row
    db_conn = pml.connect(host="localhost", user="root", password="", db="appdbproj",
                     cursorclass=pml.cursors.DictCursor)

    sql = "SELECT co.Name, cy.Name, cy.District, cy.Population \
           FROM country co \
           JOIN city cy ON co.Code = cy.CountryCode \
           WHERE co.Name LIKE %s"

    country = "%"+country+"%"

# Note - 'with' takes care of closing the connection when we are finished with it
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(sql, (country))
        results = cursor.fetchall()
        num = len(results)

# Print 2 results at a time and allow the user to quit after each 2 records by entering 'q'

    count = 0
    cont = True
    while (num>0 and cont):
        print(results[count])
        count +=1
        num -= 1
        if (count % 2) == 0:
            choice = input("-- Quit (q) --")
            if choice == 'q':
                cont = False
    if cont == True:
        choice = input("All done - press Enter to return to menu")
    return