import sqlite3
import pandas as pd

# Connect to database and create table
conn = sqlite3.connect('sports.db')
conn.execute("DROP TABLE IF EXISTS Player;")
conn.execute("""
CREATE TABLE Player (
    Player_Id INTEGER PRIMARY KEY,
    Player_Name TEXT NOT NULL UNIQUE,
    Team TEXT NOT NULL,
    Jersey_Number INTEGER,
    Is_Captain TEXT DEFAULT 'No'
);
""")
conn.commit()
print("Table created successfully!")

# Insert initial rows
conn.execute("INSERT INTO Player VALUES(1,'Lionel Messi','Inter Miami',10,'Yes');")
conn.execute("INSERT INTO Player VALUES(2,'LeBron James','LA Lakers',23,'Yes');")
conn.execute("INSERT INTO Player VALUES(3,'Patrick Mahomes','KC Chiefs',15,'No');")
conn.execute("INSERT INTO Player VALUES(4,'Erling Haaland','Man City',9,'No');")
conn.execute("INSERT INTO Player VALUES(5,'Stephen Curry','GS Warriors',30,'Yes');")
conn.execute("INSERT INTO Player(Player_Id,Player_Name,Team) VALUES(6,'Travis Kelce','KC Chiefs');")
conn.commit()
print("Rows inserted successfully!")

# Print current table status
players = pd.read_sql("SELECT * FROM Player;", conn)
print(players)

print("\n---Testing PRIMARY KEY---")
try:
    conn.execute("INSERT INTO Player VALUES(1,'Cristiano Ronaldo','Al Nassr',7,'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("PRIMARY KEY constraint failed: Player_Id must be unique!")

print("\n---Testing NOT NULL (Team)---")
try:
    conn.execute("INSERT INTO Player(Player_Id, Player_Name, Jersey_Number) VALUES(7, 'Kevin De Bruyne', 17);")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Team is NOT NULL - every row must provide a team value")

conn.close()
