class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

# If e = Employee() is an object of class employee, we can print (e.name) to print the ename by internally calling name() function.

# The method name with ‘@property’ decorator is called getter method.
# We can define a function + @ name.setter decorator like below:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Ajoy Das"
print(e.name)

e.show()