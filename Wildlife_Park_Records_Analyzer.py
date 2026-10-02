import sqlite3
import pandas as pd
conn=sqlite3.connect('wildlife_park.db')
cursor=conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Keeper;
DROP TABLE IF EXISTS Animal_Keeper;
CREATE TABLE Animal (
Animal_Id INTEGER PRIMARY KEY,
Species TEXT,
Habitat TEXT,
Age INTEGER,
Weight REAL,
Daily_Food_Lbs INTEGER
);
CREATE TABLE Keeper (
Keeper_Id INTEGER PRIMARY KEY,
Keeper_Name TEXT,
Hire_Year INTEGER,
Specialty TEXT
);
CREATE TABLE Animal_Keeper (
Animal_Id INTEGER,
Keeper_Id INTEGER
);
INSERT INTO Animal VALUES
(1,'African Lion','Savannah',8,420.5,15),
(2,'Cheetah','Savannah',4,110.2,6),
(3,'Emperor Penguin','Polar',5,75.0,4),
(4,'Polar Bear','Polar',12,900.0,30),
(5,'Red Panda','Forest',3,11.5,2),
(6,'Bengal Tiger','Forest',7,480.0,18),
(7,'Bald Eagle','Forest',6,12.0,1),
(8,'Sea Otter','Coast',5,60.0,15),
(9,'Bottlenose Dolphin','Coast',14,440.0,25),
(10,'Giant Panda','Forest',10,250.0,40),
(11,'Meerkat','Savannah',2,1.8,1),
(12,'Snow Leopard','Mountain',9,120.0,8);
INSERT INTO Keeper VALUES
(1,'Alice Smith',2015,'Mammals'),
(2,'Bob Jones',2018,'Birds'),
(3,'Charlie Brown',2020,'Aquatic'),
(4,'Diana Prince',2012,'Carnivores'),
(5,'Evan Wright',2023,'Primates');
INSERT INTO Animal_Keeper VALUES
(1,4),(2,4),(6,4),(12,4),(3,2),(7,2),(8,3),(9,3),(5,1),(10,1);
""")
conn.commit()
print('Database ready!')
habitats=pd.read_sql("""SELECT DISTINCT (Habitat) FROM Animal;""",conn)
print(habitats)
specialties=pd.read_sql("""SELECT DISTINCT (Specialty) FROM Keeper;""",conn)
print(specialties)
heavy_animals=pd.read_sql("""SELECT Species,Habitat,Weight FROM Animal ORDER BY Weight DESC;""",conn)
print(heavy_animals)
oldest_animals=pd.read_sql("""SELECT Species,Age FROM Animal ORDER BY Age DESC;""",conn)
print(oldest_animals)
newest_keepers=pd.read_sql("""SELECT Keeper_Name,Hire_Year,Specialty FROM Keeper ORDER BY Hire_Year DESC;""",conn)
print(newest_keepers)
savannah_count=pd.read_sql("""SELECT COUNT(Animal_Id) FROM Animal WHERE Habitat=='Savannah';""",conn)
print(savannah_count)
forest_food=pd.read_sql("""SELECT SUM(Daily_Food_Lbs) FROM Animal WHERE Habitat=='Forest';""",conn)
print(forest_food)
habitat_groups=pd.read_sql("""SELECT Habitat,COUNT(Animal_Id),AVG(Age),AVG(Weight) FROM Animal GROUP BY Habitat;""",conn)
print(habitat_groups)
conn.close()