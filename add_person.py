# add_person.py (Applied Databases project)
#
# A Python function to add an entry to the person table in the appdbproj database in MySQL
# Exception handling around duplicate primary keys and missing foreigh keys is done.
# Generic exceptions are also caught.
#
# Author: David O'Connell
#
# ***************************************************************************************************

import pymysql as pml
import dbconfig as cfg

def add_person(id, name, age, salary, city):

    # Use imported configuration
    host=     cfg.mysql['host']
    user=     cfg.mysql['user']
    password= cfg.mysql['password']
    database= cfg.mysql['database']

    # Use DictCursor as it is easier to get access to the attributes of the row
    db_conn = pml.connect(host=host, user=user, password=password, db=database,
                     cursorclass=pml.cursors.DictCursor)

    # Create the SQL
    sql = "INSERT INTO person VALUES (%s, %s, %s, %s, %s)"

    with db_conn:
        try:
            cursor = db_conn.cursor()
            cursor.execute(sql, (id, name, age, salary, city))
            db_conn.commit()

        except pml.err.IntegrityError as e:
            # Handle the exception for duplicate primary key and missing foreign key separately
            match e.args[0]:
                case 1062:
                    print("Error: Person ID:", id, "already exists")
                case 1452:
                    print("Error: City ID:", city, "does not exist")
                case _:
                    print(e.args)

    return