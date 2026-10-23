
import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE destination (
    destination_id INTEGER PRIMARY KEY,
    destination_name TEXT NOT NULL UNIQUE
)""")
conn.execute("""CREATE TABLE attraction (
    attraction_id INTEGER PRIMARY KEY,
    attraction_name TEXT NOT NULL,
    destination_id INTEGER
)""")
conn.executemany("INSERT INTO destination VALUES (?, ?)", [
    (1, 'Paris'),
    (2, 'Tokyo'),
    (3, 'New York'),
    (4, 'Rome'),
    (5, 'Sydney'),
    (6, 'Cairo'),
])
conn.executemany("INSERT INTO attraction VALUES (?, ?, ?)", [
    (1, 'Eiffel Tower', 1),
    (2, 'Louvre Museum', 1),
    (3, 'Shibuya Crossing', 2),
    (4, 'Mount Fuji', 2),
    (5, 'Statue of Liberty', 3),
    (6, 'Central Park', 3),
    (7, 'Colosseum', 4),
])
conn.commit()
destinations = pd.read_sql("SELECT * FROM destination;", conn)
attractions = pd.read_sql("SELECT * FROM attraction;", conn)
print("Destination table:")
print(destinations)
print()
print("Attraction table:")
print(attractions)
print()
inner = pd.read_sql(
    "SELECT destination.destination_name, attraction.attraction_name "
    "FROM destination INNER JOIN attraction ON destination.destination_id = attraction.destination_id",
    conn
)
print("INNER JOIN - destinations matched with their attractions:")
print(inner)
print()
left = pd.read_sql(
    "SELECT destination.destination_name, attraction.attraction_name "
    "FROM destination LEFT JOIN attraction ON destination.destination_id = attraction.destination_id",
    conn
)
print("LEFT JOIN - all destinations, NULL where no attraction found:")
print(left)
print()
cross = pd.read_sql(
    "SELECT destination.destination_name, attraction.attraction_name "
    "FROM destination CROSS JOIN attraction WHERE destination.destination_id <= 2",
    conn
)
print("CROSS JOIN - first 2 destinations paired with every attraction:")
print(cross)
print()
union = pd.read_sql(
    "SELECT destination_name AS name, 'Destination' as type FROM destination "
    "UNION "
    "SELECT attraction_name AS name, 'Attraction' as type FROM attraction",
    conn
)
print("UNION - Combined list of all destination and attraction names:")
print(union)
conn.close()