import psycopg2 as ps
import pandas as pd
import pandas.io.sql as sqlio
from dotenv import load_dotenv
from sqlalchemy import create_engine

df = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv')

engine = create_engine('postgresql://gitpod:postgres@localhost:5432/prueba')

con = ps.connect(dbname="prueba",
                 user="gitpod",
                 password="postgres",
                 host="localhost")

#df.to_sql('passengers', engine)

#Cuántos supervivientes hay (columna Survived)
cursor = con.cursor()
resultado = cursor.execute("""SELECT count(passengers."Survived") from passengers WHERE passengers."Survived"=1""")
resultado = cursor.fetchall()
print("Número de supervivientes = ",resultado[0][0])

#De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
cursor = con.cursor()
resultado = cursor.execute("""SELECT passengers."Sex",count(passengers."Sex") from passengers GROUP BY passengers."Sex";""")
for i in cursor:
    print(i[0],'=',i[1])
# #Cuál es el valor del ticket más caro que se compró (columna Fare)
cursor = con.cursor()
resultado = cursor.execute("""SELECT passengers."Name",passengers."Fare" from passengers WHERE passengers."Fare" = (SELECT MAX(passengers."Fare") FROM passengers )""")
resultado = cursor.fetchall()
for i in resultado:
    print("Nombre:",i[0],"Importe:",i[1])

con.close()