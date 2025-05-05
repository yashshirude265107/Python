'''Q.1) You have a list of employee records, and you need to create a new list that contains
 the names of employees who work in the 'Sales' department, all in uppercase.
 Hint:Create Dictionary with name ,department and salary field'''
 
employees = [
    {"name": "Alice", "department": "Sales", "salary": 50000},
    {"name": "Bob", "department": "HR", "salary": 45000},
    {"name": "Charlie", "department": "Sales", "salary": 55000},
    {"name": "David", "department": "IT", "salary": 60000}
]

# Create a new list for names in 'Sales' department in UPPERCASE
sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]

print(sales_employees)
