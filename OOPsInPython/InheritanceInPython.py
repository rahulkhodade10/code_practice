# parent class
class Person():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print("Name is {}".format(self.name))
        print("Id is {}".format(self.id))


# child class

class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id)

    def details(self):
        print("Name is {}".format(self.name))
        print("IdNumber: {}".format(self.id))
        print("Post: {}".format(self.post))


emp = Employee('Rahul', 886012, 200000, "Intern")
emp.display()
emp.details()
