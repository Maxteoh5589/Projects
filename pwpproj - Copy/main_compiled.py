usernames = ["benn", "max", "hugo", "john", "1"]
passwords = ["benn235", "maxtmx0", "hugo123", "122333221", "1"]
login_attempt = {user: 0 for user in usernames}

#initialisation function
# =======================================================================================================================
def initialize_files():
    files = ["ppe.txt", "suppliers.txt", "hospitals.txt", "distribution.txt"]

    for file in files:
        try:
            with open(file, 'x') as f:
                print(f"File '{file}' is created successfully.")
        except FileExistsError:
            print(f"File '{file}' exists.")
        except FileNotFoundError:
            print(f"File '{file}' not found.")

        try:
            with open(file, 'r') as f:
                content = f.read().strip()
                if not content:
                    print(f"File '{file}' is empty. Please enter data for this file.")
                    if file == "ppe.txt":
                        add_initial_data_to_inventory()
                    if file == "suppliers.txt":
                        add_initial_data_to_suppliers()
                    if file == "hospitals.txt":
                        add_initial_data_to_hospitals()
        except FileNotFoundError:
            print(f"File '{file}' not found.")

# main functions
# ======================================================================================================================
def login():
    while True:
        print("1 - Login")
        print("2 - Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            username = input("Enter username: ")
            if username not in usernames:
                print("Invalid username. Please try again.")
                continue

            password = input("Enter password: ")

            if login_attempt[username] >= 3:
                print(f"User {username} has reached the maximum number of login attempts. Access has been terminated.")
                return

            if username in usernames and password == passwords[usernames.index(username)]:
                print(f"Welcome to the Inventory Management System, {username}.")
                initialize_files()
                main_menu()
                return
            else:
                login_attempt[username] += 1
                print("Invalid password. Please try again.")

        elif choice == "2":
            print("Exiting program...")
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")


def add_initial_data_to_inventory():
    max_items = 7
    header = [["Item Code", "Item Name", "Quantity", "Supplier Code"]]
    write_data_to_file("ppe.txt", header)

    while True:
        inventory_data = read_data_from_file("ppe.txt")
        item_code = input("Enter the item code: ").strip().upper()
        item_name = input("Enter the item name: ").strip()
        quantity = input("Enter the quantity: ").strip()
        supplier_code = input("Enter the supplier code: ").strip().upper()

        if not quantity.isdigit():
            print("Invalid quantity input.")
            continue
        else:
            quantity = int(quantity)
            new_row = [item_code, item_name, str(quantity), supplier_code]

        if new_row in inventory_data:
            print("Row already exists.")
            continue
        elif item_code in column_of(0, inventory_data):
            print("Item code already exists.")
            continue
        else:
            inventory_data.append(new_row)
            write_data_to_file("ppe.txt", inventory_data)
            print("New item added.")

        if len(inventory_data) >= max_items:
            print(f"Maximum of {max_items} items reached.")
            break

        more_items = input("Do you want to add another item? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break

# initial data
# ======================================================================================================================
def add_initial_data_to_suppliers():
    max_suppliers = 3
    header = [["Supplier Code", "Supplier Name", "Contact Info", "Address"]]
    write_data_to_file("suppliers.txt", header)

    while True:
        suppliers_data = read_data_from_file("suppliers.txt")
        if len(suppliers_data) - 1 >= max_suppliers:
            print(f"Maximum amount of {max_suppliers} suppliers reached, please remove a supplier to add more.")
            break

        supplier_code = input("Enter the supplier code: ").strip().upper()
        supplier_name = input("Enter the supplier name: ").strip()
        contact_info = input("Enter the contact information: ").strip()
        address = input("Enter the address: ").strip()

        new_row = [supplier_code, supplier_name, contact_info, address]

        if new_row in suppliers_data:
            print("Row already exists.")
            continue
        elif supplier_code in column_of(0, suppliers_data):
            print("Supplier code already exists.")
            continue
        else:
            suppliers_data.append(new_row)
            write_data_to_file("suppliers.txt", suppliers_data)
            print("New supplier added.")

        more_suppliers = input("Do you want to add another supplier? (yes/no): ").strip().lower()
        if more_suppliers != 'yes':
            break


def add_initial_data_to_hospitals():
    max_hospitals = 3
    header = [["Hospital Code", "Hospital Name", "Contact Info", "Address"]]
    write_data_to_file("hospitals.txt", header)

    while True:
        hospitals_data = read_data_from_file("hospitals.txt")
        if len(hospitals_data) - 1 >= max_hospitals:
            print(f"Maximum amount of {max_hospitals} hospitals reached, please remove a hospital to add more.")
            break

        hospital_code = input("Enter the hospital code: ").strip().upper()
        hospital_name = input("Enter the hospital name: ").strip()
        contact_info = input("Enter the contact information: ").strip()
        address = input("Enter the address: ").strip()

        new_row = [hospital_code, hospital_name, contact_info, address]

        if new_row in hospitals_data:
            print("Row already exists.")
            continue
        elif hospital_code in column_of(0, hospitals_data):
            print("Hospital code already exists.")
            continue
        else:
            hospitals_data.append(new_row)
            write_data_to_file("hospitals.txt", hospitals_data)
            print("New hospital added.")

        more_hospitals = input("Do you want to add another hospital? (yes/no): ").strip().lower()
        if more_hospitals != 'yes':
            break
# menu
# ======================================================================================================================
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Inventory")
        print("2. Suppliers")
        print("3. Hospitals")
        print("4. Distribution")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            inventory_menu()
        elif choice == "2":
            suppliers_menu()
        elif choice == "3":
            hospitals_menu()
        elif choice == "4":
            distribution_menu()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def inventory_menu():
    while True:
        print("\n=== Inventory Menu ===")
        print("1. View Inventory")
        print("2. Edit Inventory")
        print("3. Return to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            inventory_data = read_data_from_file("ppe.txt")
            for row in format_matrix(inventory_data):
                print(row)

        elif choice == "2":
            supplier_data = read_data_from_file("suppliers.txt")
            inventory_code = input("Enter the item code: ").upper()
            inventory_column = input("Enter the column to change: ").title()
            inventory_value = input("Enter new value: ")
            if inventory_column == "Supplier Code":
                inventory_value = inventory_value.upper()
            else:
                pass
            if inventory_column == "Item Code" or inventory_column == "Quantity":
                print("Column cannot be edited")
                continue
            else:
                if inventory_column == "Supplier Code" and inventory_value not in column_of(0, supplier_data)[1:]:
                    print("Invalid Supplier Code input.")
                    continue
                else:
                    edit_data(inventory_code, inventory_column, inventory_value, "ppe.txt")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


def suppliers_menu():
    inventory_data = read_data_from_file("ppe.txt")

    while True:
        print("\n=== Suppliers Menu ===")
        print("1. View Suppliers")
        print("2. Edit Suppliers")
        print("3. Add Suppliers")
        print("4. Remove Supplier")
        print("5. Return to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            suppliers_data = read_data_from_file("suppliers.txt")
            for row in format_matrix(suppliers_data):
                print(row)

        elif choice == "2":
            supplier_code = input("Enter the supplier code: ").upper()
            supplier_column = input("Enter the column to change: ").title()
            supplier_value = input("Enter new value: ")
            if supplier_column == "Supplier Code":
                print("Column cannot be edited")
                continue
            else:
                edit_data(supplier_code, supplier_column, supplier_value, "suppliers.txt")

        elif choice == "3":
            suppliers_data = read_data_from_file("suppliers.txt")
            if len(suppliers_data) <= 4:
                print("Maximum amount of suppliers reach, please remove supplier to add more.")
                continue
            else:
                supplier_code = input("Enter the supplier code: ").strip().upper()
                supplier_name = input("Enter the supplier name: ").strip()
                contact_info = input("Enter the contact information: ").strip()
                address = input("Enter the address: ").strip()
                new_row = [supplier_code, supplier_name, contact_info, address]
                if new_row in suppliers_data:
                    print("Row already exist.")
                    continue
                elif supplier_code in column_of(0, suppliers_data):
                    print("Supplier code already exist.")
                    continue
                else:
                    suppliers_data.append(new_row)
                    write_data_to_file("suppliers.txt", suppliers_data)
                    print("New supplier added.")

        elif choice == "4":
            suppliers_data = read_data_from_file("suppliers.txt")
            supplier_code = input("Enter the supplier code to remove: ").strip().upper()
            if supplier_code in column_of(3, inventory_data):
                print("Supplier code exist on inventory, please change it on inventory for removal.")
                continue
            else:
                suppliers_data = [supplier for supplier in suppliers_data if
                                  supplier[0].strip().upper() != supplier_code]
                write_data_to_file("suppliers.txt", suppliers_data)
                print("Supplier removed.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def hospitals_menu():

    while True:
        print("\n=== Hospitals Menu ===")
        print("1. View Hospitals")
        print("2. Edit Hospitals")
        print("3. Add Hospitals")
        print("4. Remove Hospitals")
        print("5. Return to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hospitals_data = read_data_from_file("hospitals.txt")
            for row in format_matrix(hospitals_data):
                print(row)

        elif choice == "2":
            hospital_code = input("Enter the supplier code: ").upper()
            hospital_column = input("Enter the column to change: ").title()
            hospital_value = input("Enter new value: ")
            if hospital_column == "Hospital Code":
                print("Column cannot be edited")
                continue
            else:
                edit_data(hospital_code, hospital_column, hospital_value, "hospitals.txt")

        elif choice == "3":
            hospitals_data = read_data_from_file("hospitals.txt")
            if len(hospitals_data) <= 4:
                print("Maximum amount of hospitals reach, please remove hospital to add more.")
                continue
            else:
                hospitals_code = input("Enter the supplier code: ").strip().upper()
                hospital_name = input("Enter the supplier name: ").strip()
                contact_info = input("Enter the contact information: ").strip()
                address = input("Enter the address: ").strip()
                new_row = [hospitals_code, hospital_name, contact_info, address]
                if new_row in hospitals_data:
                    print("Row already exist.")
                    continue
                elif hospitals_code in column_of(0, hospitals_data):
                    print("Hospital code already exist.")
                    continue
                else:
                    hospitals_data.append(new_row)
                    write_data_to_file("hospitals.txt", hospitals_data)
                    print("New hospital added.")

        elif choice == "4":
            hospitals_data = read_data_from_file("hospitals.txt")
            hospital_code = input("Enter the hospital code to remove: ").strip().upper()
            hospitals_data = [hospital for hospital in hospitals_data if hospital[0].strip().upper() != hospital_code]
            write_data_to_file("hospitals.txt", hospitals_data)
            print("Hospital removed.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def distribution_menu():
    while True:
        print("\n=== Distribution Menu ===")
        print("1. Distribute Items")
        print("2. Generate Report")
        print("3. Sort Distribution by Quantity")
        print("4. Search Distribution List by Item Code")
        print("5. Return to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            distribute_items()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            sort_distributions_by_quantity()
        elif choice == "4":
            search_distribution_by_item()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
# ======================================================================================================================


# part of distribution_menu()
# ======================================================================================================================
def sort_distributions_by_quantity(descending=False):
    distribution_data = read_data_from_file("ppe.txt")

    if not distribution_data or len(distribution_data) < 2:
        print("No distribution data available to sort.")
        return

    while True:
        print("Choose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order = input("Enter your choice (1-2): ").strip().lower()
        if order == "1":
            descending = False
            break
        elif order == "2":
            descending = True
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 2.")

    headers = distribution_data[0]
    data_rows = distribution_data[1:]

    sorted_data = sorted(data_rows, key=lambda x: int(x[2]), reverse=descending)
    sorted_data.insert(0, headers)

    print(f"Distribution data sorted by Quantity ({'Descending' if descending else 'Ascending'}):")
    for row in format_matrix(sorted_data):
        print(row)

# Example usage:
# sort_distributions_by_quantity("distribution.txt", descending=True)

def distribute_items():
    inventory_data = read_data_from_file("ppe.txt")
    hospitals_data = read_data_from_file("hospitals.txt")
    distribution_data = read_data_from_file("distribution.txt")

    if len(distribution_data) == 0:
        headers = [["Item Code", "Hospital Code", "Quantity", "Supplier Code"]]
        write_data_to_file("distribution.txt", headers)
        distribution_data = headers

    low_stock_items = [item for item in inventory_data[1:] if int(item[2]) <= 25]
    if low_stock_items:
        print("Items with quantity less than or equal to 25:")
        for item in low_stock_items:
            print(f"Item Code: {item[0]}, Quantity: {item[2]}")
    else:
        print("No items with quantity less than or equal to 25.")

    item_code = input("Enter the item code: ").strip().upper()
    hospital_code = input("Enter the hospital code: ").strip().upper()
    quantity = input("Enter the quantity to distribute: ").strip()

    if not quantity.isdigit():
        print("Invalid quantity input.")
        return
    else:
        quantity = int(quantity)

    if item_code in column_of(0, inventory_data):
        searched = [item for item in inventory_data if item[0] == item_code][0]
        if int(searched[2]) >= quantity:
            searched[2] = str(int(searched[2]) - quantity)
            supplier_code = searched[3]
        else:
            print("Insufficient quantity in inventory.")
            return
    else:
        print("Invalid item code.")
        return

    if hospital_code in column_of(0, hospitals_data):
        distribution_data.append([item_code, hospital_code, str(quantity), supplier_code])
        write_data_to_file("ppe.txt", inventory_data)
        write_data_to_file("distribution.txt", distribution_data)
        print(f"Distributed {quantity} of item code {item_code} to hospital code {hospital_code}.")

    else:
        print("Invalid hospital code.")
        return
def generate_report():
    distribution_data = read_data_from_file("distribution.txt")[1:]

    supplier_report = {}
    hospital_report = {}
    transaction_report = {}

    for distribution in distribution_data:
        item_code, hospital_code, quantity, supplier_code = distribution

        # Update supplier report
        if supplier_code in supplier_report:
            supplier_report[supplier_code].append((item_code, quantity))
        else:
            supplier_report[supplier_code] = [(item_code, quantity)]

        # Update hospital report
        if hospital_code in hospital_report:
            hospital_report[hospital_code].append((item_code, quantity))
        else:
            hospital_report[hospital_code] = [(item_code, quantity)]

        # Update transaction report
        key = (hospital_code, supplier_code)
        if key in transaction_report:
            transaction_report[key] += int(quantity)
        else:
            transaction_report[key] = int(quantity)

    supplier_report_data = [["Supplier Code", "Item Code", "Quantity"]]
    for supplier_code, items in supplier_report.items():
        for item_code, quantity in items:
            supplier_report_data.append([supplier_code, item_code, quantity])

    print("\n=== Supplier Report ===")
    for supplier_code, items in supplier_report.items():
        print(f"Supplier Code: {supplier_code}")
        for item_code, quantity in items:
            print(f"  Item Code: {item_code}, Quantity: {quantity}")

    hospital_report_data = [["Hospital Code", "Item Code", "Quantity"]]
    for hospital_code, items in hospital_report.items():
        for item_code, quantity in items:
            hospital_report_data.append([hospital_code, item_code, quantity])

    print("\n=== Hospital Report ===")
    for hospital_code, items in hospital_report.items():
        print(f"Hospital Code: {hospital_code}")
        for item_code, quantity in items:
            print(f"  Item Code: {item_code}, Quantity: {quantity}")

    transaction_report_data = [["Hospital Code", "Supplier Code", "Total Quantity"]]
    for (hospital_code, supplier_code), total_quantity in transaction_report.items():
        transaction_report_data.append([hospital_code, supplier_code, total_quantity])

    print("\n=== Transaction Report ===")
    for row in format_matrix(transaction_report_data):
        print(row)

def search_distribution_by_item():
    distribution_data = read_data_from_file("distribution.txt")
    header = distribution_data[0]

    item_code = input("Enter the item code to search: ").strip().upper()

    filtered_data = [distribution for distribution in distribution_data if distribution[0].strip().upper() == item_code]
    filtered_data.insert(0, header)

    if not filtered_data[1:]:
        print("No distributions found for the given item code.")
    else:
        for distribution in format_matrix(filtered_data):
            print(distribution)
# ======================================================================================================================


# small functions
# ======================================================================================================================
def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for row in data:
            file.write('|'.join(row) + '\n')
        file.close()


def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data = [line.strip().split('|') for line in lines]
        return data
    except FileNotFoundError:
        return []


def column_of(index, data):
    rotated_data = [item for item in zip(*data)]
    return rotated_data[int(index)]


def format_matrix(data):
    if not data:
        return []

    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*data)]

    formatted_rows = []
    for row in data:
        formatted_rows.append(
            "| " + " | ".join(f"{str(cell).ljust(width)}" for cell, width in zip(row, col_widths)) + " |"
        )

    return formatted_rows

def edit_data(code, column, new_value, file_path):
    data = read_data_from_file(file_path)
    if code in column_of(0, data)[1:] and column in data[0]:
        for row in data[1:]:
            if row[0] == code:
                row[data[0].index(column)] = new_value
                write_data_to_file(file_path, data)
                print("Edit successful.")
                return
            else:
                pass
    else:
        print(f"Invalid {data[0][0]} or column.")
        return
# ======================================================================================================================

if __name__ == "__main__":
    login()
