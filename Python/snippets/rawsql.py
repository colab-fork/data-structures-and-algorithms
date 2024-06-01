import sqlite3

def connect_to_db(db_path):
    print("Connecting... ")
    return sqlite3.connect(db_path)

if __name__ == "__main__":
    with connect_to_db("birds.db") as connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS bird (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL
        );
""")


"""
$ python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import connect_to_db
>>> connection = connect_to_db("birds.db")
Connecting... 
>>> cursor = connection.cursor()
>>> CREATE_BIRDS_SQL = """
... INSERT INTO
... bird (name)
... VALUES
... ('Humming Bird'),
... ('Sugar Glider');
... """
>>> cursor.execute(CREATE_BIRDS_SQL)
<sqlite3.Cursor object at 0x000001EE18C8F4C0>
>>> connection.commit()
>>> READ_BIRDS_SQL = "SELECT * from bird"
>>> cursor.execute(READ_BIRDS_SQL)
<sqlite3.Cursor object at 0x000001EE18C8F4C0>
>>> cursor.fetchall()
[(1, 'Humming Bird'), (2, 'Sugar Glider')]
>>> UPDATE_HUMMINGBIRD_SQL = """
... UPDATE
... bird
... SET 
... name = "Hummingbird"
... WHERE 
... id = 1
... """
>>> cursor.execute(UPDATE_HUMMINGBIRD_SQL)
<sqlite3.Cursor object at 0x000001EE18C8F4C0>
>>> connection.commit()
>>> DELETE_SUGAR_GLIDER_SQL = "Delete FROM bird WHERE id=2"
>>> cursor.execute(DELETE_SUGAR_GLIDER_SQL)
<sqlite3.Cursor object at 0x000001EE18C8F4C0>
>>> connection.commit()
>>> connection.close()

"""
