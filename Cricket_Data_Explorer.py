import sqlite3
import pandas as pd
conn=sqlite3.connect('cricket.db')
cursor=conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;
CREATE TABLE Team (
Team_Id INTEGER PRIMARY KEY,
Team_Name TEXT
);
CREATE TABLE Match (
Match_Id INTEGER PRIMARY KEY,
Season_Id INTEGER,
Match_Winner INTEGER,
Win_Margin INTEGER
);
CREATE TABLE Player_Match (
Match_Id INTEGER,
Player_Id INTEGER
);
INSERT INTO Team VALUES
(1,'Chennai Super Kings'),(2,'Delhi Capitals'),
(3,'Deccan Chargers'),(4,'Delhi Daredevils'),
(5,'Mumbai Indians'),(6,'Kolkata Knight Riders'),
(7,'Rajasthan Royals'),(8,'Kings XI Punjab');
INSERT INTO Match VALUES
(1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
(5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),
(9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);
INSERT INTO Player_Match VALUES
(1,101),(1,102),(2,103),(3,101),(4,104),(5,102);
""")
conn.commit()
print('Database ready!')
tables=pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""",conn)
print(tables)
matches=pd.read_sql("""SELECT *
    FROM Match;""",conn)
print(matches)
print('Rows and columns:',matches.shape)
teams=pd.read_sql("""SELECT *
    FROM Team;""",conn)
print(teams)
team_names=pd.read_sql("""SELECT Team_Id, Team_name
    FROM Team;""",conn)
print(team_names)
player_matches=pd.read_sql("""SELECT Match_Id,Player_Id
    FROM Player_Match;""",conn)
print(player_matches)
rr_wins=pd.read_sql("""SELECT *
    FROM Match
    WHERE Match_Winner==7;""",conn)
print(rr_wins)
mi_recent=pd.read_sql("""SELECT *
    FROM Match
    WHERE Match_Winner==5 AND Season_Id IN (8,9);""",conn)
