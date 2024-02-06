import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id})"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return f"Department: {self.name}"


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print(f"Department '{department_name}' does not exist.")

    def display_departments(self):
        for department_name, department in self.departments.items():
            print(department)

    def save_data(self, file_path):
        data = {"departments": {}}
        for department_name, department in self.departments.items():
            data["departments"][department_name] = {
                "employees": [
                    {"name": emp.name, "emp_id": emp.emp_id, "title": emp.title, "department": emp.department}
                    for emp in department.employees
                ]
            }
        with open(file_path, "w") as file:
            json.dump(data, file)

    def load_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                for department_name, department_data in data["departments"].items():
                    new_department = Department(department_name)
                    for emp_data in department_data["employees"]:
                        new_employee = Employee(
                            emp_data["name"], emp_data["emp_id"], emp_data["title"], emp_data["department"]
                        )
                        new_department.add_employee(new_employee)
                    self.departments[department_name] = new_department
        except FileNotFoundError:
            print("File not found. Starting with an empty company.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty company.")


def menu():
    print("Employee Management System Menu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Display Departments")
    print("4. Add Employee")
    print("5. Remove Employee")
    print("6. Display Employees in Department")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")


def main():
    company = Company()

    while True:
        menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            department_name = input("Enter the department name: ")
            new_department = Department(department_name)
            company.add_department(new_department)
            print(f"Department '{department_name}' added.")

        elif choice == "2":
            department_name = input("Enter the department name to remove: ")
            company.remove_department(department_name)

        elif choice == "3":
            company.display_departments()

        elif choice == "4":
            department_name = input("Enter the department name to add an employee: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                new_employee = Employee(name, emp_id, title, department_name)
                company.departments[department_name].add_employee(new_employee)
                print(f"Employee '{name}' added to department '{department_name}'.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == "5":
            department_name = input("Enter the department name to remove an employee: ")
            if department_name in company.departments:
                emp_id = input("Enter employee ID to remove: ")
                company.departments[department_name].remove_employee(emp_id)
                print(f"Employee with ID '{emp_id}' removed from department '{department_name}'.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == "6":
            department_name = input("Enter the department name to display employees: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == "7":
            file_path = input("Enter the file path to save data: ")
            company.save_data(file_path)
            print(f"Data saved to {file_path}.")

        elif choice == "8":
            file_path = input("Enter the file path to load data: ")
            company.load_data(file_path)
            print(f"Data loaded from {file_path}.")

        elif choice == "9":
            print("Exiting the Employee Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
