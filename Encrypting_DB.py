import pymysql
import mysql.connector
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
    
# result = cur.execute("Select Company, Model,Mileage, Engine, Engine_type, Price FROM ice_cars")#"Select name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details")
# row = cur.fetchall()

r2 = cur1.execute("SELECT * FROM User_details")
row2 = cur1.fetchall()


num = 0
for i in row2 :
    print(i)
    l = []
    num += 1
    for j in i :
        if type(j) == int :
            l.append(j)
            #print(j)
        else:
            l.append(str(Crypt(j).encrypt()))
    print(l[1])
    #cur1.execute(f"Insert INTO animal_details VALUES ({l[0]}, {l[1]}, {l[2]}, {l[3]}, {l[4]}, {l[5]}, {l[6]}, {l[7]}, )")
    #cur.execute ("INSERT INTO animal_details (name, kingdom, phylum, class, naturalorder, family, genus, species, active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8],l[9]))
    #cur.execute ("INSERT INTO User_details (Username, Gmail, Password, Active) VALUES (%s,%s,%s,%s)", (l[1], l[2], l[3], l[4]))
    # values = (l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8],l[9])
    # cur.execute(temp_qry, values)
    con.commit()
    #cur.execute(f"Insert INTO animal_details VALUES ({l[0]}, {l[1]}, {l[2]}, {l[3]}, {l[4]}, {l[5]}, {l[6]}, {l[7]}, {l[8]}, {l[9]})")

# for i in row :
#     print(i)
#     l = []
#     num += 1
#     for j in i :
#         print(j)
    
    # if num :
    #     temp_qry = str("INSERT INTO animal_details (name, kingdom, phylum, class, naturalorder, family, genus, species) VALUES (?,?,?,?,?,?,?,?)",((l[0]), l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
    #     cur.execute(temp_qry)
    
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
cur1.close()
con1.close()