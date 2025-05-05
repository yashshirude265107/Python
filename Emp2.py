class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_bonus(self):
        bonus = self.salary * 0.10
        self.salary += bonus
        return bonus

emp = Employee("Alice", 50000, "HR")

print("Name:", emp.name)
print("Department:", emp.department)
print("Original Salary:", emp.salary)

bonus = emp.give_bonus()
print("Bonus Given:", bonus)
print("Updated Salary:", emp.salary)
