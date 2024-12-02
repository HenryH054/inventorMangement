import csv
import os

def add_row(file_name, row_data):
    file_exists = os.path.isfile(file_name)
    
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            header = ['ModelNumber', 'SerialNumber']
            writer.writerow(header)
        
        writer.writerow(row_data)
        print(f"Row {row_data} added successfully.")

def remove_row(file_name, serial):
    rows = []
    
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if len(rows) > 1:
        try:
            for i in rows:
                if i[1] == serial:
                    serial = i
            removed_row = rows.remove(serial)
            print(f"Row {removed_row} removed successfully.")
            
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        except:
            print("argg")
            raise(Exception(f"Error: Could not remove {serial} from file."))
    else:
        raise(Exception("Error: No rows to remove or invalid input."))

def display_csv(file_name):
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            x = 0
            columns = []
            json = []
            for row in reader:
                if x == 0:
                    for header in row:
                        columns.append(header)
                    x += 1
                else:
                    rowJson = {}
                    for info in range(len(row)):
                        rowJson[columns[info]] = row[info]
                    json.append(rowJson)
            return json

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")

def main():
    file_name = 'example.csv'
    
    while True:
        print("\nCSV File Management")
        print("1. Add a row")
        print("2. Remove a row")
        print("3. Display file contents")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            row_data = input("Enter row data separated by commas (EG: Model Number, Serial Number): ")
            row_data = row_data.split(',')
            add_row(file_name, row_data)
        
        elif choice == '2':
            display_csv(file_name)
            try:
                row_index = int(input("Enter the row number to remove (starting from 1): ")) - 1
                remove_row(file_name, row_index)
            except ValueError:
                print("Invalid input. Please enter a valid row number.")
        
        elif choice == '3':
            display_csv(file_name)
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")
