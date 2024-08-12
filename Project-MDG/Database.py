import sqlite3

# Create or connect to the database
conn = sqlite3.connect('mdg_inventory.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT,
    mileage INTEGER
)
''')

conn.commit()
conn.close()
