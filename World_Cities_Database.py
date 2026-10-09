# ============================================================

# SQL Constraints

# Activity: World Cities Database

# ============================================================

# ---- PART 1: Create the Table with Constraints ----

# SQL constraints are rules written inside CREATE TABLE.

# They control what data each column is allowed to store.

# If a row breaks a constraint, the insert is rejected.

# Constraints keep the database accurate and reliable.

import sqlite3

import pandas as pd

conn = sqlite3.connect('cities.db')

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""

CREATE TABLE City (

City_Id INTEGER PRIMARY KEY,

City_Name TEXT NOT NULL UNIQUE,

Country TEXT NOT NULL,

Population INTEGER,

Is_Capital TEXT DEFAULT 'No'

);

""")

conn.commit()

print("Table created successfully!")
conn.execute("INSERT INTO City VALUES(1,'Tokyo','Japan',13960000,'Yes');")
conn.execute("INSERT INTO City VALUES(2,'Nairobi','Kenya',4397000,'Yes');")
conn.execute("INSERT INTO City VALUES(3,'Mumbai','India',20667656,'No');")
conn.execute("INSERT INTO City VALUES(4,'Sao Paulo','Brazil',12325232,'No');")
conn.execute("INSERT INTO City VALUES(5,'London','UK',9541000,'Yes');")
conn.execute("INSERT INTO City(City_Id,City_name,Country)VALUES(6,'Sydney','Australia');")
conn.commit()
print("Rows inserted successfully!")
cities=pd.read_sql("SELECT*FROM City;",conn)
print(cities)
print("\n---Testing PRIMARY KEY---")
try:
    conn.execute("INSERT INTO City VALUES(1,'Cairo','Egypt',21323000,'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print()