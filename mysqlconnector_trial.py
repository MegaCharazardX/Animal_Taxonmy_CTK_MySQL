#import mysql.connector
import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database = "animal_taxonomy_db"
                            )


cur = con.cursor()

# if con.is_connected():
#     print(1)
    
result = cur.execute("Select * FROM animal_details")
row = cur.fetchall()
#print(row)
for i in row :
    print(i)
 
cur.close()
con.close()