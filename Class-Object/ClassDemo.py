class Employee:
    language = "Py" #class attribute
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good morning")

Ajoy = Employee()
Ajoy.name = "Ajoy" #Instance attribute
print(Ajoy.name, Ajoy.language, Ajoy.salary)

Ajoy.getInfo()  # It automatically convert this to Employee.getInfo(Ajoy)

# Here name is instance attribute and salary and language are class attibutes as they directly belong to the class.

# Instance attributes, take preference over class attributes during assignment & retrieval.