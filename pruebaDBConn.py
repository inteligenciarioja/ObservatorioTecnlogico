import MySQLdb

print("Me estoy conectando")

db_connection = MySQLdb.connect(host='localhost',db='exampledb',
                                user='exampleuser', passwd='pimylifeup')

print("Me he conectado")

c = db_connection.cursor()
c.execute("INSERT INTO exampledb.example (id, name, job) VALUES ('8', 'Joaquin', 'Estanquero')")
c.execute("SELECT * FROM exampledb.example")
print (c.fetchall)

for row in c.fetchall() :
    print(row)
