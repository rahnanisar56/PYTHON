class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Person Details")
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id

    def show_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)

class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours

    def show_details(self):
        print("Part-Time Worker Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)

class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print("Consultant Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)

person1 = Person("Rahul", 25)
person1.show_details()

employee1 = Employee("Anjali", 30, "EMP101")
employee1.show_details()

parttime1 = PartTime("Vikram", 22, 5.5)
parttime1.show_details()

consultant1 = Consultant("Sneha", 35, "CONS201", 6.0, "Website Development")
consultant1.show_details()