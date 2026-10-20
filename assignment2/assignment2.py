import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    emp_dict = {}
    emp_list = []
    
    try:
        with open("../csv/employees.csv") as employee_file:
            csv_data = csv.reader(employee_file)
            
            for i, row in enumerate(csv_data):
                if i == 0:
                    emp_dict["fields"] = row
                    continue
                
                emp_list.append(row)
                
            emp_dict["rows"] = emp_list
            
        return emp_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        
        for trace in trace_back:
            stack_trace.append(f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}")
        
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        
        if message:
            print(f"Exception message: {message}")
            
        print(f"Stack trace: {stack_trace}")
    
employees = read_employees() or {}

# Task 3
def column_index(column: str):
    return employees["fields"].index(column)

employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_num: int):
    index = column_index("first_name")
    return employees["rows"][row_num][index]

# Task 5
def employee_find(employee_id: int):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=filter(employee_match, employees["rows"])
    return list(matches)

# Task 6
def employee_find_2(employee_id: int):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

# Task 7
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]

# Task 8
def employee_dict(row: list) -> dict:
    headers = employees["fields"]
    emp_dict = {}
    
    for i, header in enumerate(headers):
        if header == "employee_id":
            continue
        
        emp_dict[header] = row[i]
        
    return emp_dict

# Task 9
def all_employees_dict():
    rows = employees["rows"]
    emps_dict = {}
    
    for row in rows:
        id = row[0]
        emps_dict[id] = employee_dict(row)
        
    return emps_dict

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret: str):
    custom_module.set_secret(new_secret)
    
set_that_secret("my_secret")

# Task 12
def read_minutes():
    def csv_to_dict(link: str):
        d = {}
        l = []
        
        try:
            with open(link) as m:
                cs = csv.reader(m)
                
                for i, row in enumerate(cs):
                    if i == 0:
                        d["fields"] = tuple(row)
                        continue
                    
                    l.append(tuple(row))
                                    
                d["rows"] = l
                
            return d
                
        except Exception as e:
            print(e)
    
    return csv_to_dict("../csv/minutes1.csv"), csv_to_dict("../csv/minutes2.csv")

minutes1, minutes2 = read_minutes()

# Task 13
def create_minutes_set():
    global minutes1, minutes2
    minutes1 = minutes1 or {}
    minutes2 = minutes2 or {}
    return set(minutes1["rows"]) | set(minutes2["rows"])

minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    min_list = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), min_list))

minutes_list = create_minutes_list()

# Task 15
def write_sorted_list():
    global minutes1, minutes2
    minutes1 = minutes1 or {}
    minutes2 = minutes2 or {}
    minutes_list.sort(key=lambda x: x[1])
    min_list_converted = map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    
    with open("./minutes.csv", "w", newline="") as m_csv:
        writer = csv.writer(m_csv)
        writer.writerow(minutes1["fields"])
        writer.writerows(minutes1["rows"])
        
    return list(min_list_converted)