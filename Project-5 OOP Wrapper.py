class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, e_id, salary):
        super().__init__(name, age)
        self.e_id = e_id
        self.salary = salary

    def get_e_id(self):
        return self.e_id

    def set_e_id(self, e_id):
        self.e_id = e_id

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self.e_id}")
        print(f"Salary: ${self.salary}")

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.e_id}, Salary: ${self.salary}"
    
    def __lt__(self, other):
        return self.salary < other.salary


class Manager(Employee):
    def __init__(self, name, age, e_id, salary, dept):
        super().__init__(name, age, e_id, salary)
        self.dept = dept

    def display(self):
        super().display()
        print(f"Department: {self.dept}")
        print("Role: Manager")

    def __str__(self):
        return f"Manager: {self.name}, ID: {self.e_id}, Salary: ${self.salary}, Department: {self.dept}"


persons = []
employees = []

def create_person():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    person = Person(name, age)
    persons.append(person)
    print(f"Person created with name: {name} and age: {age}.")

def create_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    employee = Employee(name, age, emp_id, salary)
    employees.append(employee)
    print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

def create_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    dept = input("Enter Department: ")
    manager = Manager(name, age, emp_id, salary, dept)
    employees.append(manager)
    print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")


def show_details():
    print("Choose details to show:")
    print("1. Person\n2. Employee\n3. Manager")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        if not persons:
            print("No persons found.")
            return
        for p in persons:
            p.display()
            print("-" * 20)
    elif choice == 2:
        if not employees:
            print("No employees found.")
            return
        for e in employees:
            e.display()
            print("-" * 20)
    elif choice == 3:
        managers = [e for e in employees if isinstance(e, Manager)]
        if not managers:
            print("No managers found.")
            return
        for m in managers:
            m.display()
            print("-" * 20)

def compare_salaries():
    if len(employees) < 2:
        print("Need at least 2 employees.")
        return
    
    id1 = input("Enter first employee ID: ")
    id2 = input("Enter second employee ID: ")
    
    emp1 = next((e for e in employees if e.e_id == id1), None)
    emp2 = next((e for e in employees if e.e_id == id2), None)
    
    if not emp1 or not emp2:
        print("Employee not found.")
        return
    
    if emp1.salary == emp2.salary:
        print("Both have same salary.")
    else:
        higher = emp1 if emp1.salary > emp2.salary else emp2
        print(f"{higher.name} has higher salary.")

print("--- Python OOP Project: Employee Management System ---")

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee") 
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        create_person()
    elif choice == 2:
        create_employee()
    elif choice == 3:
        create_manager()
    elif choice == 4:
        show_details()
    elif choice == 5:
        compare_salaries()
    elif choice == 6:
        print("Exiting the system. All resources have been freed.")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
