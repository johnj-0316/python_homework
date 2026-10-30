import pandas as pd

# Task 1
#1
task1_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(task1_dict)

#2
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70_000, 80_000, 90_000]

#3
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1

#4
task1_older.to_csv("./employees.csv", index=False)


# Task 2
#1
task2_employees = pd.read_csv("./employees.csv")

#2
json_employees = pd.read_json("./additional_employees.json")

#3
more_employees = pd.concat([task2_employees, json_employees]).reset_index(drop=True)


# Task 3
#1
first_three = more_employees.head(3)

#2
last_two = more_employees.tail(2)

#3
employee_shape = more_employees.shape

#4
print(more_employees.info())


# Task 4
#1
dirty_data = pd.read_csv("./dirty_data.csv")
clean_data = dirty_data.copy()

#2
clean_data.drop_duplicates(inplace=True)

#3
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

#4
clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA).replace("n/a", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

#5
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

#6
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed")

#7
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()