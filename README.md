# Applied_Databases
Repo for Applied Databases course


## Assumptions and Interpretations

For the successful use cases, the screenshots show the menu following the printing out of the results. There is no "Press Enter to continue" prompt. Therefore, bearing in mind that we had to have the *exact* answer for the database query results, I am taking the same approach with the Python program and implementing the specification and screenshots as exactly as possible.

### Deprecated functions
The neo4j driver is old and functions have since been deprecated. These will continue to be used

### 4.4.7.1 
In Part 2, a 'valid' city could be interpreted in 2 ways  
  
a) Valid means that it is in neo4j.  
b) Valid means that it may not be in neo4j but is in mysql.  
  
The option implemented is a). There is no point in adding the city to neo4j if it cannot be twinned with Dublin, since that would be the reason for adding it. So, if it is not in neo4j, the user will be returned to the main menu.



## Packages installed
Successfully installed pymysql-1.1.0
Successfully installed neo4j-5.20.0
C:\Users\dvdge\Documents\HDIP\APPLIED_DATABASES\Python\neo4jtest.py:37: DeprecationWarning: read_transaction has been renamed to execute_read
  values1, values2 = session.read_transaction(get_cities)

From [neo4j docs (Python Driver Manual 5)](https://neo4j.com/docs/python-manual/current/transactions/)
  The methods .execute_read() and .execute_write() have replaced .read_transaction() and .write_transaction(), which are deprecated in version 5.x and will be removed in version 6.0.