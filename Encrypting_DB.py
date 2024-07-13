import pymysql
from Crypter import Crypter as Crypt
import sqlite3

f = open("Encrypted_Data.txt", "wb+")
con1 = sqlite3.connect("Animal_Taxonomy_Db.db", timeout = 3)

cur1 = con1.cursor() 

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database = "animal_taxonomy_db"
                    )


cur = con.cursor()

# if con.is_connected():
#     print(1)
    
result = cur.execute("Select name FROM animal_details")#"Select name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details")
row = cur.fetchall()

r2 = cur1.execute("SELECT name , kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details")
row2 = cur1.fetchall()


for i in row2 :
    print(i)
    l = []
    for j in i :
        print(j)
        l.append(str(Crypt(j).encrypt()))
    print(l)
    
    if 
    temp_qry = str("INSERT INTO animal_details (name, kingdom, phylum, class, naturalorder, family, genus, species) VALUES (?,?,?,?,?,?,?,?)",((l[0]), l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
    cur.execute(temp_qry)
    
# #print(row)
# num = 0
# for i in row :
#     print(i)
#     num += 1
#     for j in i :
#         a = Crypt(j).encrypt()
#         #result1 = cur.execute("UPDATE animal_details SET ")#"Select name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details")
#         # row1 = cur.fetchall()
#         # a = Crypt(j).encrypt()
#         print(j)

f.close()
cur.close()
con.close()