import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY, 
        title TEXT,
        pages INTEGER, 
        current_page INTEGER
    )
""")

# cursor.execute("""
#     INSERT INTO book VALUES (
#         0, "A Great book", 213, 27
#     )
# """)

# cursor.execute("""
#     INSERT INTO book VALUES (
#         1, "B Great book", 137, 33
#     )
# """)

connection.commit()

rows = cursor.execute("""
    SELECT title, pages, current_page FROM book
""")

for rows in rows:
    print(rows)
connection.close()