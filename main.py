#Write a program to create a parent class Person (attributes - name, id number) 
# with a method display to display the attributes. 
# Next, create a child class Employee (attributes - name, id number, salary, post). 
# Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and 
# id number.
class Person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
        print(self.salary)
        print(self.post)
class Employee(Person):
    def __init__(self,salary,post,name,id_number):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id_number)
ob=Employee("15000","seneor engineer","Jake","15670")
ob.display()