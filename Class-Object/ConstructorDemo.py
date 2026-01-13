class Employee:
    language = "Py" #class attribute
    salary = 1200000
    
    def __init__(self, name, salary, language): #Dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good morning")

Ajoy = Employee("Ajoy", 1300000, "JavaScript")
# Ajoy.name = "Ajoy" #Instance attribute

print(Ajoy.name, Ajoy.salary, Ajoy.language)
