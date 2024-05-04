# cities_by_country.py (Applied Databases project)
#
# A Python function to retrieve the cities in a given country from the city table in the
# appdbproj database in MySQL
# They are printed 2 at a time unless the user enters 'q' to exit to the main menu. Once complete, the user is
# returned to the main menu. 
# 
# Author: David O'Connell
#
# ***************************************************************************************************

import pymysql as pml
import dbconfig as cfg

def country_pop(gle, pop):

    # Use imported configuration
    host=     cfg.mysql['host']
    user=     cfg.mysql['user']
    password= cfg.mysql['password']
    database= cfg.mysql['database']

    # Use DictCursor as it is easier to get access to the attributes of the row
    db_conn = pml.connect(host=host, user=user, password=password, db=database,
                     cursorclass=pml.cursors.DictCursor)

    # Build the sql string. A bit ugly, but could not get this to work with inserting 
    # one of <, >, = as a string. I may revisit if I have time. We know gle is one of
    # <, >, = as it has been checked by the calling program.
    match gle:
        case '<':
            sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population < %s"
        case '>':
            sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population > %s"
        case '=':
            sql = "SELECT Code, Name, Continent, Population FROM country WHERE Population = %s"

    # 'with' takes care of closing the connection when we are finished with it
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(sql, (pop))
        results = cursor.fetchall()
        
        if len(results) == 0:
            print("No countries meet the criteria.")
        
        else:
            # Print the results
            for result in results:
                for x in result:
                    print(result[x], "| ", end='')
                print("\b\b  ")
    
    return