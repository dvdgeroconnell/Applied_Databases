## Innovations
Just a couple of things to mention here - and these aren't really innovations, just good coding practise.
1. Separate out the credentials into a separate config file, which is included in the .gitignore file so it is not uploaded to GitHub. This was covered in the Web Services & Applications module.
2. On exiting the program I had occasionally been seeing the following message:   
*Failed to write data to connection IPv4Address(('localhost', 7687)) (ResolvedIPv4Address(('127.0.0.1', 7687)))*
I thought this may be because the connection was still open, so I changed the creation of the driver to the following, which worked.  
*with gdb.driver(uri, auth=(user,password), max_connection_lifetime=1000) as driver:*
