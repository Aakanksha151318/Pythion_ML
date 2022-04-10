import mysql.connector
conn = mysql.connector.connect(user = 'root',host = 'localhost',password='dhananjay151318@@')
print(conn)

asd = conn.cursor()
asd.execute("SHOW DATABASES")
for d in asd:
    print(d)

myc = conn.cursor()
myc.execute('CREATE DATABASE pdb')
myc.close()




