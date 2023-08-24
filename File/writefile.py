def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for emp_name, address in data.items():
            file.write(f"{emp_name}: {address}\n")

if __name__ == "__main__":
    employees_data = {
        "John Doe": "123 Main St, Cityville",
        "Jane Smith": "456 Elm St, Townsville",
        "Michael Johnson": "789 Oak St, Villageland",
        "Emily Brown": "101 Pine St, Hamletville"
    }

    file_path = "File/employees.txt"
    write_to_file(file_path, employees_data)
    print(f"Data has been written to '{file_path}'.")
