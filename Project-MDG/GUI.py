import tkinter as tk
from tkinter import messagebox
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER,
            color TEXT,
            mileage INTEGER
        )
        ''')
        self.conn.commit()

    def add_vehicle(self, make, model, year, color, mileage):
        self.cursor.execute('''
        INSERT INTO vehicles (make, model, year, color, mileage) VALUES (?, ?, ?, ?, ?)
        ''', (make, model, year, color, mileage))
        self.conn.commit()

    def view_inventory(self):
        self.cursor.execute('SELECT * FROM vehicles')
        return self.cursor.fetchall()

    def delete_vehicle(self, vehicle_id):
        self.cursor.execute('DELETE FROM vehicles WHERE id = ?', (vehicle_id,))
        self.conn.commit()

    def update_vehicle(self, vehicle_id, make, model, year, color, mileage):
        self.cursor.execute('''
        UPDATE vehicles SET make = ?, model = ?, year = ?, color = ?, mileage = ? WHERE id = ?
        ''', (make, model, year, color, mileage, vehicle_id))
        self.conn.commit()

    def close(self):
        self.conn.close()

class InventoryApp:
    def __init__(self, root, db_name):
        self.db = Database(db_name)
        self.root = root
        self.root.title("MDG Automotive Inventory")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        self.make_label = tk.Label(self.root, text="Make")
        self.make_label.grid(row=0, column=0)
        self.make_entry = tk.Entry(self.root)
        self.make_entry.grid(row=0, column=1)

        self.model_label = tk.Label(self.root, text="Model")
        self.model_label.grid(row=1, column=0)
        self.model_entry = tk.Entry(self.root)
        self.model_entry.grid(row=1, column=1)

        self.year_label = tk.Label(self.root, text="Year")
        self.year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.grid(row=2, column=1)

        self.color_label = tk.Label(self.root, text="Color")
        self.color_label.grid(row=3, column=0)
        self.color_entry = tk.Entry(self.root)
        self.color_entry.grid(row=3, column=1)

        self.mileage_label = tk.Label(self.root, text="Mileage")
        self.mileage_label.grid(row=4, column=0)
        self.mileage_entry = tk.Entry(self.root)
        self.mileage_entry.grid(row=4, column=1)

        self.add_button = tk.Button(self.root, text="Add Vehicle", command=self.add_vehicle)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.view_button = tk.Button(self.root, text="View Inventory", command=self.view_inventory)
        self.view_button.grid(row=6, column=0, columnspan=2)

        self.inventory_listbox = tk.Listbox(self.root, width=50)
        self.inventory_listbox.grid(row=7, column=0, columnspan=2)

        self.delete_button = tk.Button(self.root, text="Delete Vehicle", command=self.delete_vehicle)
        self.delete_button.grid(row=8, column=0, columnspan=2)

        self.update_button = tk.Button(self.root, text="Update Vehicle", command=self.update_vehicle)
        self.update_button.grid(row=9, column=0, columnspan=2)

    def add_vehicle(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        color = self.color_entry.get()
        mileage = int(self.mileage_entry.get())

        self.db.add_vehicle(make, model, year, color, mileage)
        messagebox.showinfo("Success", "Vehicle added successfully")
        self.clear_entries()

    def view_inventory(self):
        self.inventory_listbox.delete(0, tk.END)
        vehicles = self.db.view_inventory()
        for vehicle in vehicles:
            self.inventory_listbox.insert(tk.END, f"ID: {vehicle[0]}, Make: {vehicle[1]}, Model: {vehicle[2]}, Year: {vehicle[3]}, Color: {vehicle[4]}, Mileage: {vehicle[5]}")

    def delete_vehicle(self):
        selected_item = self.inventory_listbox.get(tk.ACTIVE)
        if selected_item:
            vehicle_id = int(selected_item.split(",")[0].split(":")[1])
            self.db.delete_vehicle(vehicle_id)
            messagebox.showinfo("Success", "Vehicle deleted successfully")
            self.view_inventory()

    def update_vehicle(self):
        selected_item = self.inventory_listbox.get(tk.ACTIVE)
        if selected_item:
            vehicle_id = int(selected_item.split(",")[0].split(":")[1])
            make = self.make_entry.get()
            model = self.model_entry.get()
            year = int(self.year_entry.get())
            color = self.color_entry.get()
            mileage = int(self.mileage_entry.get())

            self.db.update_vehicle(vehicle_id, make, model, year, color, mileage)
            messagebox.showinfo("Success", "Vehicle updated successfully")
            self.clear_entries()
            self.view_inventory()

    def clear_entries(self):
        self.make_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.mileage_entry.delete(0, tk.END)

    def close(self):
        self.db.close()

# Run the application
root = tk.Tk()
app = InventoryApp(root, 'mdg_inventory.db')
root.mainloop()
