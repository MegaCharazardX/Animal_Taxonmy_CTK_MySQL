import pymysql # I use this but you can use any 
# OR
import mysql.connector

# IF NEED install pip by running :
# "pip install pymysql"

con = pymysql.connect( # Connection String for mysql.connector is given in the text book
    host = "localhost",
    user = "root",
    passwd  = "Your Password",
    database = "Your database"
                    )


cur = con.cursor() # Establish your cursor

#For SELECT Query :-
r = cur.execute("Your Query") # Enter your Query for Example : SELECT * FROM <tbl>
for i in r:
    print(i)
    
# For Command Queries:- 
cur.execute("Your Query") # Enter your Query for Example : DELETE, UPDATE, INSERT Queries

cur.close() # Close the  cursor NOT NEEDED
con.commit() # Close the  connection NEEDED MUST

# This editor that I'm using is called Visual Studio Code
# If you want to use this Just text me, i'll tell you what to do.
"😁😁"