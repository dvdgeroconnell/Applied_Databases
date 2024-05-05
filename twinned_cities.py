# twinned_cities.py (Applied Databases project)
#
# A Python function to return the list of twinned cities from the neo4j database and
# print them out in the required format.
#
# Author: David O'Connell
#
# ***************************************************************************************************

from neo4j import GraphDatabase as gdb
import dbconfig as cfg

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
    
    # Use imported configuration
    uri =      cfg.neo4j['uri']
    user =     cfg.neo4j['user']
    password = cfg.neo4j['password']

    #uri = "neo4j://localhost:7687"
    with gdb.driver(uri, auth=(user,password), max_connection_lifetime=1000) as driver:

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