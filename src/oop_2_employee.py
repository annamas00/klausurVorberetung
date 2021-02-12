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
    pass

    def __init__(self, name1, department1):
        self.name = name1
        self.department = department1

    def __str__(self):
        out = "This person's name ist " + self.name
        out += " and he is from " + self.department + " depatment"
        return out
    def set_name(self, name):
        self.name=name
    def set_department(self, department):
        self.department = department

    def dictionary(self):
        # return self.name + self.department
        print("<", self.name, ">, <", self.department, ">")

if __name__ == "__main__":
    print("Employee application")
    emp1 = Employee("Anne", "Finance")
    print(emp1)
    emp2 = Employee("Stefan", "IT")
    print(emp2)
    emp3 = Employee("Joe", "Finance")
    print(emp3)
    #emp1.dictionary()
   # emp2.dictionary()
   # Employee.accounts_info()
    dic = {}
    #dic[emp1] = [emp1]
    dic[emp1.department] = [emp1]
    dic[emp2.department] = [emp2]
    dic[emp3.department].append(emp3)
    for d in dic:
        print(d)