class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Role:", self.role)
        print()


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print("Trainer Details")
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print()


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Yoga Instructor Details")
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)
        print()


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        self.yoga_style = yoga_style

    def display(self):
        print("Multi-Trainer Details")
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
        print()


# Creating objects and displaying details

emp = Employee("Rahul", "Staff")
emp.display()

trainer = Trainer("Anjali", "Trainer", "Weight Training")
trainer.display()

yoga = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
yoga.display()

multi = MultiTrainer("Arjun", "Multi Trainer", "Fitness Coaching", "Vinyasa Yoga")
multi.display()