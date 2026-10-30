# Task 3
import csv

def read_employees():
    employee_rows = []
    
    with open("../csv/employees.csv") as file:
        reader = csv.DictReader(file)
        
        for rows in reader:
            employee_rows.append(rows)
            
    employee_names = [f"{row['first_name']} {row['last_name']}" for row in employee_rows]
    employee_names_with_e = [name for name in employee_names if "e" in name]
    print(employee_names)
    print(employee_names_with_e)

read_employees()