# add_person.py (Applied Databases project)
#
# A Python function to add an entry to the person table in the appdbproj database in MySQL
# Exception handling around duplicate primary keys and missing foreigh keys is done.
# Generic exceptions are also caught.
#
# Author: David O'Connell
#
# ***************************************************************************************************

#import pymysql as pml
from neo4j import GraphDatabase as gdb

def check_city(tx, id):

    query = "MATCH(c:City{cid:$city_id}) RETURN c.name"
    results = tx.run(query, city_id=int(id))
    name = []
    for result in results:
        name.append(result['c.name'])
    if name == []:
        name.append('')

    return name[0]


def check_twinned(tx, id):
    # This function checks if the target city is already twinned wiht Dublin.
    query = "MATCH (c:City{cid:$city_id})-[:TWINNED_WITH]-(:City{name:'Dublin'}) RETURN c.name"
    results = tx.run(query, city_id=int(id))
    name = []
    for result in results:
        name.append(result['c.name'])
    if name == []:
        name.append('')

    return name[0]


def create_new_city(city):
    print("Retrieving city id", city, "from mysql, adding to neo4j")


def new_twin(tx, city):
    # City exists in the neo4j database, create the TWINNED_WITH relationship
    query = "MATCH(c1:City{name:'Dublin'}), (c2:City{cid:$city_id}) \
             CREATE (c1)<-[t:TWINNED_WITH]-(c2) RETURN c2.name, t"
    results = tx.run(query, city_id=int(city))
    # result = results.single()
    name = []
    for result in results:
        name.append(result['c.name']) # this one.....
    if name == []:
        name.append('')

    return name[0]

def create_twin(twin):

    # This is the main function called from the main menu. It  makes use of the other
    # functions in this file.

    uri = "neo4j://localhost:7687"
    driver = gdb.driver(uri, auth=("neo4j","dave1234"), max_connection_lifetime=1000)

    with driver.session() as session:
        #Check if city is in the neo4j database
        city = session.read_transaction(check_city, twin)
        if city =='':
            print("No such city in database")
            create_new_city(twin)
        else:
            print("city:", city)
            # City exists in the neo4j database. Check if it is already twinned.
            twinned = session.read_transaction(check_twinned, twin)

            if twinned =='':
                print("Need to create TWINNED WITH relationship")
                session.write_transaction(new_twin, twin)
                print("Dublin is now twinned with", city)

            else:
                # It is already twinned - this is the message in the Specification
                print("Dublin is now twinned with", city)
    return