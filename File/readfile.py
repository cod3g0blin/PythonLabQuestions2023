def read_from_file(file_path):
    employees_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            emp_name, address = line.split(": ",1)
            employees_data[emp_name] = address
    return employees_data

if __name__ == "__main__":
    file_path = "File/employees.txt"
    employees_data = read_from_file(file_path)

    print("Employee records:")
    for emp_name, address in employees_data.items():
        print(f"{emp_name}: {address}")
