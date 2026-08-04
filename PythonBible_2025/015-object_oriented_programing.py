'''Classes and Objects In Python, a class is a plan or template for building objects. It specifies a set of characteristics and actions that the objects generated from the class will have. To generate an object from a class, you have to first define the class. Here's an example of a simple class definition in Python: class Person:

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    def say_hello(self):
        return f"Hello, {self.name} and I'm {self.age} years old!"

'''In this example, we establish a class named "Person" with two attributes (name and age) and one method (say_hello). The init method is a unique method that is triggered when an object is generated from the class. It initializes the attributes of the object with the values passed as arguments to the constructor. The self parameter refers to the object that is being created. To generate an object from the Person class, we can use the following code:'''

person1 = Person("Alice", 30)
print(person1.greet())
print(person1.say_hello())

'''this generates an object of the pPerson class with the name "alice" and age 30. We can access the attributes and methods of the object using the dot notation: '''

print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
'''Methods and Attributes: 
In python, methods are functions that are fedined insde a class and can manipulate the attributes of the object. These attributes are variables that store the state of the object. The Person class example above has attributes of name and age. Methods are used to perate on these attributes or provide specific functionality to the object. The code provides an example of a class with two methods. '''

class Rectangle: 

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(5, 10)
print(rectangle1.area())  # Output: 50
print(rectangle1.perimeter())  # Output: 30

