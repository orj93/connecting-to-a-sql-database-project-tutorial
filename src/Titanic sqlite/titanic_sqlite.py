import sqlite3
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv')

con = sqlite3.connect("titanic.db")
#df.to_sql('passengers', con, if_exists='replace')

# Cuántos supervivientes hay (columna Survived)
cursor = con.execute("SELECT count(survived) from passengers WHERE Survived=1")
for i in cursor:
    print("Número de supervivientes = ",i[0])

#De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)

cursor = con.execute("SELECT sex,count(sex) from passengers GROUP BY sex")
for i in cursor:
    print(i[0],'=',i[1])

# Cuál es el valor del ticket más caro que se compró (columna Fare)

cursor = con.execute("SELECT  name,fare from passengers WHERE fare = (SELECT MAX(Fare) FROM passengers)")
for i in cursor:
    print("Nombre:",i[0],"Importe:",i[1])

con.close()