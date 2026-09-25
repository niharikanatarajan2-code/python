import sqlite3
import pandas as pd
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS Book_Borrowing;
CREATE TABLE Book (
    Book_Id INTEGER PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    Page_Count INTEGER,
    Publication_Year INTEGER
);
CREATE TABLE Author (
    Author_Id INTEGER PRIMARY KEY,
    Author_Name TEXT
);
CREATE TABLE Book_Borrowing (
    Match_Id INTEGER PRIMARY KEY,
    Book_Id INTEGER,
    Borrow_Count INTEGER
);
INSERT INTO Book VALUES
(1, 'The Great Gatsby', 'Fiction', 180, 1925),
(2, 'To Kill a Mockingbird', 'Fiction', 281, 1960),
(3, 'A Brief History of Time', 'Science', 212, 1988),
(4, 'The Hobbit', 'Fantasy', 310, 1937),
(5, '1984', 'Dystopian', 328, 1949),
(6, 'The Catcher in the Rye', 'Fiction', 277, 1951),
(7, 'Brave New World', 'Dystopian', 268, 1932),
(8, 'Cosmos', 'Science', 365, 1980);
INSERT INTO Book_Borrowing VALUES
(1, 1, 45), (2, 2, 88), (3, 3, 12), (4, 4, 67),
(5, 5, 95), (6, 6, 34), (7, 7, 23), (8, 8, 50);
""")
conn.commit()
print('Library Database Ready!\n') 
print("--- All Books ---")
books = pd.read_sql("SELECT * FROM Book;", conn)
print(books)
print('\nRows and columns of Book table:', books.shape)
print("\n--- Filtered: Fiction Books > 200 Pages ---")
filtered_books = pd.read_sql("""
    SELECT * 
    FROM Book 
    WHERE Genre = 'Fiction' AND Page_Count > 200;
""", conn)
print(filtered_books)
print("\n--- Pattern Search: Titles containing 'The' ---")
pattern_search = pd.read_sql("""
    SELECT * 
    FROM Book 
    WHERE Title LIKE '%The%';
""", conn)
print(pattern_search)
print("\n--- Aggregation: Smallest and Largest Page Counts ---")
min_max_pages = pd.read_sql("""
    SELECT MIN(Page_Count) AS Shortest_Book, MAX(Page_Count) AS Longest_Book 
    FROM Book;
""", conn)
print(min_max_pages)
conn.close()
