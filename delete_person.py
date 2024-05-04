# delete_person.py (Applied Databases project)
#
# A Python function to delete a person from the person table in the appdbproj database in MySQL.
# It must first be established whether they have visited cities or not; if they have, they should
# not be deleted.
# Generic exceptions are caught and printed. The user is returned to the main menu. 
#
# Author: David O'Connell
#
# ***************************************************************************************************

import pymysql as pml
import dbconfig as cfg

def delete_person(delete_id):

    # Use imported configuration
    host=     cfg.mysql['host']
    user=     cfg.mysql['user']
    password= cfg.mysql['password']
    database= cfg.mysql['database']

    # Use DictCursor as it is easier to get access to the attributes of the row
    db_conn = pml.connect(host=host, user=user, password=password, db=database,
                     cursorclass=pml.cursors.DictCursor)

    # First check if that person has visited a city - if so, they must not be deleted
    sql = "SELECT vc.personID, vc.cityID FROM hasvisitedcity vc \
           JOIN person p ON p.personID = vc.personID \
            WHERE P.personID = %s"

    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(sql, (delete_id))
        results = cursor.fetchall()
        num = len(results)
        delete = True

        # If the person has visited cities, results will have one or more entries.
        if num > 0:
            print("Error: Can't delete Person ID:", delete_id, "\b. He/she has visited cities.")
            delete = False

    if delete:
        # Good to delete - connection needs to be restablished
        db_conn = pml.connect(host="localhost", user="root", password="", db="appdbproj",
                              cursorclass=pml.cursors.DictCursor)

        del_sql = "DELETE FROM person WHERE personID = %s"

        with db_conn:
            try:
                cursor = db_conn.cursor()
                cursor.execute(del_sql, (delete_id))
                db_conn.commit()
                deleted_rowcount = cursor.rowcount

                # Database does not return an error if that person ID did not exist in the
                # database, but the affected rowcount is 0. Check for this.
                if deleted_rowcount == 0:
                    print("Error: Person ID:",delete_id,"does not exist." )
                    delete = False

            except pml.err.IntegrityError as e:
                # Generic exception handling - just print the error.
                print(e.args)
                delete = False

    return delete