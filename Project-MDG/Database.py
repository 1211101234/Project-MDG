import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS vehicles (
                            id INTEGER PRIMARY KEY,
                            make TEXT,
                            model TEXT,
                            year INTEGER,
                            color TEXT,
                            mileage INTEGER)""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tools (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            quantity INTEGER,
                            condition TEXT)""")
        self.conn.commit()

    def add_vehicle(self, make, model, year, color, mileage):
        self.cur.execute("INSERT INTO vehicles (make, model, year, color, mileage) VALUES (?, ?, ?, ?, ?)",
                         (make, model, year, color, mileage))
        self.conn.commit()

    def add_tool(self, name, quantity, condition):
        self.cur.execute("INSERT INTO tools (name, quantity, condition) VALUES (?, ?, ?)",
                         (name, quantity, condition))
        self.conn.commit()

    def view_inventory(self):
        self.cur.execute("SELECT * FROM vehicles")
        rows = self.cur.fetchall()
        return rows

    def view_tools(self):
        self.cur.execute("SELECT * FROM tools")
        rows = self.cur.fetchall()
        return rows

    def delete_vehicle(self, vehicle_id):
        self.cur.execute("DELETE FROM vehicles WHERE id=?", (vehicle_id,))
        self.conn.commit()

    def delete_tool(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE id=?", (tool_id,))
        self.conn.commit()

    def update_vehicle(self, vehicle_id, make, model, year, color, mileage):
        self.cur.execute("""UPDATE vehicles SET make=?, model=?, year=?, color=?, mileage=?
                            WHERE id=?""", (make, model, year, color, mileage, vehicle_id))
        self.conn.commit()

    def update_tool(self, tool_id, name, quantity, condition):
        self.cur.execute("""UPDATE tools SET name=?, quantity=?, condition=?
                            WHERE id=?""", (name, quantity, condition, tool_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
