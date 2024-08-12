import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Database import Database

class InventoryApp:
    def __init__(self, root, db_name):
        self.root = root
        self.db = Database(db_name)
        self.root.title("MDG Inventory System")
        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self.root)
        
        self.vehicle_tab = tk.Frame(self.tab_control)
        self.tool_tab = tk.Frame(self.tab_control)
        
        self.tab_control.add(self.vehicle_tab, text="Vehicles")
        self.tab_control.add(self.tool_tab, text="Tools")
        self.tab_control.pack(expand=1, fill="both")
        
        self.create_vehicle_tab()
        self.create_tool_tab()

    def create_vehicle_tab(self):
        tk.Label(self.vehicle_tab, text="Make").grid(row=0, column=0, padx=10, pady=5)
        self.make_entry = tk.Entry(self.vehicle_tab)
        self.make_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.vehicle_tab, text="Model").grid(row=1, column=0, padx=10, pady=5)
        self.model_entry = tk.Entry(self.vehicle_tab)
        self.model_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.vehicle_tab, text="Year").grid(row=2, column=0, padx=10, pady=5)
        self.year_entry = tk.Entry(self.vehicle_tab)
        self.year_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.vehicle_tab, text="Color").grid(row=3, column=0, padx=10, pady=5)
        self.color_entry = tk.Entry(self.vehicle_tab)
        self.color_entry.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.vehicle_tab, text="Mileage").grid(row=4, column=0, padx=10, pady=5)
        self.mileage_entry = tk.Entry(self.vehicle_tab)
        self.mileage_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

        self.add_vehicle_button = tk.Button(self.vehicle_tab, text="Add Vehicle", command=self.add_vehicle)
        self.add_vehicle_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_inventory_button = tk.Button(self.vehicle_tab, text="View Inventory", command=self.view_inventory)
        self.view_inventory_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.vehicle_tree = ttk.Treeview(self.vehicle_tab, columns=("ID", "Make", "Model", "Year", "Color", "Mileage"), show='headings')
        self.vehicle_tree.heading("ID", text="ID")
        self.vehicle_tree.heading("Make", text="Make")
        self.vehicle_tree.heading("Model", text="Model")
        self.vehicle_tree.heading("Year", text="Year")
        self.vehicle_tree.heading("Color", text="Color")
        self.vehicle_tree.heading("Mileage", text="Mileage")
        self.vehicle_tree.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        self.delete_vehicle_button = tk.Button(self.vehicle_tab, text="Delete Vehicle", command=self.delete_vehicle)
        self.delete_vehicle_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.update_vehicle_button = tk.Button(self.vehicle_tab, text="Update Vehicle", command=self.update_vehicle)
        self.update_vehicle_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.vehicle_tab.columnconfigure(1, weight=1)
        self.vehicle_tab.rowconfigure(7, weight=1)

    def create_tool_tab(self):
        tk.Label(self.tool_tab, text="Tool Name").grid(row=0, column=0, padx=10, pady=5)
        self.tool_name_entry = tk.Entry(self.tool_tab)
        self.tool_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.tool_tab, text="Quantity").grid(row=1, column=0, padx=10, pady=5)
        self.tool_quantity_entry = tk.Entry(self.tool_tab)
        self.tool_quantity_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.tool_tab, text="Condition").grid(row=2, column=0, padx=10, pady=5)
        self.tool_condition_entry = tk.Entry(self.tool_tab)
        self.tool_condition_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        self.add_tool_button = tk.Button(self.tool_tab, text="Add Tool", command=self.add_tool)
        self.add_tool_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_tools_button = tk.Button(self.tool_tab, text="View Tools", command=self.view_tools)
        self.view_tools_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.tool_tree = ttk.Treeview(self.tool_tab, columns=("ID", "Name", "Quantity", "Condition"), show='headings')
        self.tool_tree.heading("ID", text="ID")
        self.tool_tree.heading("Name", text="Name")
        self.tool_tree.heading("Quantity", text="Quantity")
        self.tool_tree.heading("Condition", text="Condition")
        self.tool_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        self.delete_tool_button = tk.Button(self.tool_tab, text="Delete Tool", command=self.delete_tool)
        self.delete_tool_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.update_tool_button = tk.Button(self.tool_tab, text="Update Tool", command=self.update_tool)
        self.update_tool_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.tool_tab.columnconfigure(1, weight=1)
        self.tool_tab.rowconfigure(5, weight=1)

    def convert_to_int(self, value):
        try:
            return int(value.replace(' ', ''))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return None

    def add_vehicle(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        color = self.color_entry.get()
        mileage = self.mileage_entry.get()
        if make and model and year and color and mileage:
            year = self.convert_to_int(year)
            mileage = self.convert_to_int(mileage)
            if year is not None and mileage is not None:
                self.db.add_vehicle(make, model, year, color, mileage)
                messagebox.showinfo("Success", "Vehicle added successfully!")
                self.view_inventory()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_tool(self):
        name = self.tool_name_entry.get()
        quantity = self.tool_quantity_entry.get()
        condition = self.tool_condition_entry.get()
        if name and quantity and condition:
            quantity = self.convert_to_int(quantity)
            if quantity is not None:
                self.db.add_tool(name, quantity, condition)
                messagebox.showinfo("Success", "Tool added successfully!")
                self.view_tools()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_inventory(self):
        self.vehicle_tree.delete(*self.vehicle_tree.get_children())
        for row in self.db.view_inventory():
            self.vehicle_tree.insert('', 'end', values=row)

    def view_tools(self):
        self.tool_tree.delete(*self.tool_tree.get_children())
        for row in self.db.view_tools():
            self.tool_tree.insert('', 'end', values=row)

    def delete_vehicle(self):
        selected_item = self.vehicle_tree.selection()
        if selected_item:
            vehicle_id = self.vehicle_tree.item(selected_item, 'values')[0]
            self.db.delete_vehicle(vehicle_id)
            self.view_inventory()
        else:
            messagebox.showerror("Error", "Please select a vehicle to delete.")

    def delete_tool(self):
        selected_item = self.tool_tree.selection()
        if selected_item:
            tool_id = self.tool_tree.item(selected_item, 'values')[0]
            self.db.delete_tool(tool_id)
            self.view_tools()
        else:
            messagebox.showerror("Error", "Please select a tool to delete.")

    def update_vehicle(self):
        selected_item = self.vehicle_tree.selection()
        if selected_item:
            vehicle_id = self.vehicle_tree.item(selected_item, 'values')[0]
            make = self.make_entry.get()
            model = self.model_entry.get()
            year = self.year_entry.get()
            color = self.color_entry.get()
            mileage = self.mileage_entry.get()
            if make and model and year and color and mileage:
                year = self.convert_to_int(year)
                mileage = self.convert_to_int(mileage)
                if year is not None and mileage is not None:
                    self.db.update_vehicle(vehicle_id, make, model, year, color, mileage)
                    messagebox.showinfo("Success", "Vehicle updated successfully!")
                    self.view_inventory()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select a vehicle to update.")

    def update_tool(self):
        selected_item = self.tool_tree.selection()
        if selected_item:
            tool_id = self.tool_tree.item(selected_item, 'values')[0]
            name = self.tool_name_entry.get()
            quantity = self.tool_quantity_entry.get()
            condition = self.tool_condition_entry.get()
            if name and quantity and condition:
                quantity = self.convert_to_int(quantity)
                if quantity is not None:
                    self.db.update_tool(tool_id, name, quantity, condition)
                    messagebox.showinfo("Success", "Tool updated successfully!")
                    self.view_tools()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select a tool to update.")

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("MDG logo.ico")
    app = InventoryApp(root, "mdg_inventory.db")
    root.mainloop()
