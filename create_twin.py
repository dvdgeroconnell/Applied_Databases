# create_twin.py (Applied Databases project)
#
# This file includes a set of Python functions to query and update the neo4j database.
# The user is asked to enter the ID of a city to be twinned with Dublin in neo4j
# Scenario 1: the city doesn't exist in neo4j so it is retried from mysql, added to 
# neo4jand twinned with Dublin
# Scenario 2: the city exists in neo4j and is twinned with Dublin.
# Scenario 3: the city is already twinned with Dublin so no action is taken.
# Error Condition 1: The city does not exist in MySQL - the 


# 7add an entry to the person table in the appdbproj database in MySQL
# Exception handling around duplicate primary keys and missing foreigh keys is done.
# Generic exceptions are also caught.
#
# Author: David O'Connell
#
# ***************************************************************************************************

from neo4j import GraphDatabase as gdb
import pymysql as pml
import dbconfig as cfg

#-----------------------------------------------------------------------------------
# This function checks if a city exists in the neo4j database.

def check_city(tx, id):

    query = "MATCH(c:City{cid:$city_id}) RETURN c.name"
    results = tx.run(query, city_id=int(id))
    name = []
    for result in results:
        name.append(result['c.name'])
    if name == []:
        name.append('')

    return name[0]

#-----------------------------------------------------------------------------------
# This function creates a city in the neo4j database.

def create_neo4j_city(tx, city, name):
            
    query = "CREATE(c:City{cid:$cityid,name:$cityname}) RETURN c.id, c.name"
    created = tx.run(query, cityid=int(city), cityname = name)
    response_name = []
    for result in created:
        response_name.append(result['c.name'])
    if response_name == []:
        response_name.append('')
    return response_name[0]

#-----------------------------------------------------------------------------------
# This function checks if the target city is already twinned with Dublin.

def check_twinned(tx, id):

    query = "MATCH (c:City{cid:$c_id})-[:TWINNED_WITH]-(:City{name:'Dublin'}) RETURN c.name"
    results = tx.run(query, c_id=int(id))
    name = []
    for result in results:
        name.append(result['c.name'])
    if name == []:
        name.append('')

    return name[0]

#-----------------------------------------------------------------------------------
# This function retrieves a city from mysql and adds it to neo4j.

def retrieve_city_from_mysql(city):

    # Use imported configuration
    host=     cfg.mysql['host']
    user=     cfg.mysql['user']
    password= cfg.mysql['password']
    database= cfg.mysql['database']

    # Use DictCursor as it is easier to get access to the attributes of the row
    db_conn = pml.connect(host=host, user=user, password=password, db=database,
                     cursorclass=pml.cursors.DictCursor)

    # Build the sql string.
    sql = "SELECT Name FROM city WHERE ID = %s"

    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(sql, (city))
        # We expect one (or no) result, as ID is a primary key
        result = cursor.fetchone()

        # City ID doesn't exist in MySQL
        if not result:
            print("City ID:", city, "doesn't exist in MySQL database\n")
            name = ''
            found = False
        else:
            name = (result['Name'])
            #print("City ID:", city, "Name:", name, "found in MySQL")
            found = True

    return found, name

#-----------------------------------------------------------------------------------
# This function creates the :TWINNED_WITH relationship for a target city that exists
# in the neo4j database, but is not twinned with Dublin. 

def new_twin(tx, city):

    twinned = False
    query = "MATCH(c1:City{name:'Dublin'}), (c2:City{cid:$city_id}) \
             CREATE (c1)<-[t:TWINNED_WITH]-(c2) RETURN c2.name, t"

    result = tx.run(query, city_id=int(city)).single()
    if result:
        name = []
        name.append(result['c2.name'])
        if name == []:
            name.append('')
        twinned = True
    return twinned

#-----------------------------------------------------------------------------------
# This is the primary function called from the main menu. It  makes use of the 
# other functions above.

def create_twin(twin):

    dublin = 1447
    outcome=False

    # Use imported configuration
    uri =      cfg.neo4j['uri']
    user =     cfg.neo4j['user']
    password = cfg.neo4j['password']

    with gdb.driver(uri, auth=(user, password), max_connection_lifetime=1000) as driver:

        with driver.session() as session:
            # Check if city is in the neo4j database
            dublin_exists = session.read_transaction(check_city, dublin)
            city = session.read_transaction(check_city, twin)

            if dublin_exists != '':
                # If the city does not exist in the neo4j database, retrieve from MySQL.
                if city == '':
                    # print("Scenario 1")
                    exists, city = retrieve_city_from_mysql(twin)

                    if exists:
                        # city is in MySQL, add to neo4j. No need for 'else', just return False.
                        session.write_transaction(create_neo4j_city, twin, city)
                        outcome=True
                else:
                    exists = True

                if exists:
                    # City (now) exists in the neo4j database. Check if it is already twinned.
                    # It won't be if it was just added, so the check is redundant in that case.
                    twinned = session.read_transaction(check_twinned, twin)
                    if twinned =='':
                        print("I shouldn't be here")
                        checked = session.write_transaction(new_twin, twin)
                        if checked:
                            print("Dublin is now twinned with", city)
                            outcome=True
                        # No need for else - "outcome = False" doesn't change.

                    else:
                        # Already twinned - the message in the Specification says "now", not "already"
                        print("Dublin is now twinned with", city)
                        outcome=True
            else:
                outcome=True
                print("Error: Dublin does not exist in Neo4j database")
    return outcome