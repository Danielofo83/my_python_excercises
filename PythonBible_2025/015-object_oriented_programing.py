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


'''Methods and Attributes In Python, methods are functions that are defined inside a class and can manipulate the attributes of the object. These attributes are variables that store the state of the object. The Person class example above has attributes of name and age. Methods are used to operate on these attributes or provide specific functionality to the object. The code provides an example of a class with two methods.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

'''This particular example demonstrates the creation of a class named Rectangle which contains two attributes: width and height, as well as two methods: area and perimeter. The area method returns the calculated area of the rectangle, whereas the perimeter method returns the calculated perimeter of the rectangle. To instantiate an object of the Rectangle class, you can use the provided code:'''

rectangle1 = Rectangle(20,10)

'''This creates an object of the rectangle class with a witdth. of 10 and a height of 20. WE can call the methods of the object using the dot notation:'''
print(rectangle1.area())
print(rectangle1.perimeter())

'''Attributes can aslo be accessed onad modified directly , without using a method. example is below'''

class Counter: 
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

'''INHERITANCE 
In object oriented programming, inheritance is a useful conect that enables us to form new classes by building upon existing ones. By inheriting from an existing class, we can create a new class called a child class, with the existing class becoming the parent class or superclass


THE BENEFITS OF INHERITING PROPERTIES AND METHODS FROM PARENT CLASSES

Inheritance enables us to utilize the properties and methdos of an existing class in a new class. Whenever a child class inherits from a parent class, ti gains access to all of the properties and methods of the paret class. this makes it easier to create a new classes that have similiar functionality to existing classes without having to duplicate code. This promotes code reusability and reduces the amount of code that needs to be written, making it easier to maintain and update the codebase.

To inherit from a parent class, we simply define the child class with the parent class as a parameter in the class definition. For example, to create a new class called Car that inherits from the Vehicle class, we would define it as follows:

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def honk(self):
        return "Honk honk!"
'''

 class Car(Vehicle):
    pass

'''Now, the Car class has access to all the properties and methods of the Vehicle class. We can also override the properties and methods of the parent class if we want to change their behavior in the child class.

CREATING CHILD CLASSES
Inheritance also allows us to create more specialized classes based on existing classes. For example, we could create a Truck class that inherits from the Vehicle class but has additional properties and methods specific to trucks. To create a child class with additional properties and methods, we simply define them in the child class. For example:
'''

class Truck(Vehicle):
    def _init__(self,make,model,year,payload_capacity):
        super().__init__(make,model,year)
        self.year = year
        self.payload_capacity = payload_capacity

    def load_cargo(self,weight):
        if weight <= self.payload_capacity:
            return f"Loading {weight} kg of cargo."
        else:
            return "Cargo exceeds payload capacity."

'''Here the Truck class inherits from the vehicle class and adds a payload capacity attribute and a load_cargo method. The load_cargo method checks if the weight of the cargo being loaded is within the payload capacity of the truck and returns a message indicating whether the cargo can be loaded or not.

POLYMORPHISM
Polymorphism is another important concept in object-oriented programming. It allows us to use the same interface to represent different types of objects. This means that we can write code that works with objects of different classes, as long as they implement the same interface.

Using polymorphism in Python In Python, we can use polymorphism with any object that implements the same methods or has the same attributes. For example, we could write a function that takes a list of objects and calls a draw method on each of them, regardless of their class:'''

def draw_all(objects):
    for obj in objects:
        obj.draw()

'''Here, the draw_all function takes a list of objects and calls the draw method on each of them. As long as each object has a draw method, this function will work correctly.

 POLYMORPHISM IN INHERITANCE
  
    In the context of object-oriented programming, polymorphism refers to an object's capacity to adapt to different situations and take on multiple roles. This can be achieved through inheritance, where a child class inherits properties and methods from a parent class but can also modify or replace them to suit its specific requirements.

 OVERRIDING METHODS
  
    When a child class inherits from a parent class, it can override methods defined in the parent class by redefining them in the child class. This allows the child class to customize the behavior of inherited methods to suit its own needs. When a method is called on an instance of the child class, the method defined in the child class will be used instead of the method defined in the parent class. For example, let's say we have a parent class called Animal with a method called speak():'''

class Animal:   
    def speak(self):
        return "Animal makes a sound"

#now let's create a child class called Dog that inherits from the Animal class and overrides the speak() method to provide a specific implementation for dogs:

class Dog(Animal):
    def speak(self):
        return "Dog barks"
