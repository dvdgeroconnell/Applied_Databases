# add_person.py (Applied Databases project)
#
# A Python function to add an entry to the person table in the appdbproj database in MySQL
# Exception handling around duplicate primary keys and missing foreigh keys is done.
# Generic exceptions are also caught.
#
# Author: David O'Connell
#
# ***************************************************************************************************

from neo4j import GraphDatabase as gdb

def get_cities(tx):

    query = "MATCH (c1:City)-[:TWINNED_WITH]-(c2:City) \
             RETURN c1.name, c2.name ORDER BY c1.name"
    
    results = tx.run(query)
    names1 = []
    names2 = []
    for result in results:
        names1.append(result['c1.name'])
        names2.append(result['c2.name'])
    return names1, names2

def twinned_cities():

    uri = "neo4j://localhost:7687"
    driver = gdb.driver(uri, auth=("neo4j","dave1234"), max_connection_lifetime=1000)
    #print("connected: {}".format(driver.verify_connectivity()))
    #print(driver.execute_query("SHOW HOME DATABASE").records[0]["name"])

    with driver.session() as session:
        #res = session.run("SHOW DATABASES yield name;")
        #for i in res:
        #    print(i['name'])
        values1, values2 = session.read_transaction(get_cities)
        print("\nTwinned Cities")
        print("--------------")
        entries = len(values1)
        for name in range(entries):
            print(values1[name],"<->",values2[name])

    return