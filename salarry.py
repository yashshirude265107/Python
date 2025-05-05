# WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary  
# to employee if the salary is more than 50000 .calculate total salary.

basic_salary = float(input("Enter basic salary: "))

# Check if salary is more than 50000
if basic_salary > 50000:
    da = 0.10 * basic_salary  # 10% DA
    hra = 0.12 * basic_salary  # 12% HRA
    total_salary = basic_salary + da + hra
    print(f"DA: ₹{da}")
    print(f"HRA: ₹{hra}")
    print(f"Total Salary: ₹{total_salary}")
else:
    print(f"Total Salary: ₹{basic_salary} (No DA or HRA applied)")
