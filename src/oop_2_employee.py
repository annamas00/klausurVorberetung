"""Exercise 2: (5 points)

a) Write the complete code for the Employee class (including
   constructor, __str__, ...). (2 points)

b) Create a main application, create a few employee objects and show
   how you can manipulate them using the methods. (1 point)

c) Create a department dictionary (dictionary of strings to lists/sets
   of employees) with at least two departments (e.g. "accounting",
   "sales", ...) with each at least two employees. Print for each
   employee in the dictionary "<department> <employee name>".
   (2 points)

"""


class Employee:
    def __init__(self, name, department):
        self.firstName = name
        self.dep = department

    def set_name(self, name):
        self.firstName = name

    def set_department(self, department):
        self.dep = department

    def print_dict(self):
        print("<", self.name, ">, <", self.department, ">")

    def __str__(self):
        res = "*** Worker Info ***\n\n"
        res += "Name: " + self.firstName + "\n"
        res += "Department: " + self.dep + "\n\n"
        return res


if __name__ == "__main__":
    print("Employee application")
    miles = Employee("Miles", "sales")
    print(miles)
    miles.set_name("Michael")
    print(miles)
    miles.print_dict()
