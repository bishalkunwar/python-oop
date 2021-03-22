#python code to use class and objects:
class Person:
 
    # init method or constructor 
    def __init__(self, name):
        self.name = name
 
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)
 
p = Person('Shwetanshu')
p.say_hi()

#python code to implement class and instance variables:
class CSStudent:
 
    # Class Variable
    stream = 'cse'            
 
    # The init method or constructor
    def __init__(self, roll):
   
        # Instance Variable    
        self.roll = roll       
  
# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)
  
print(a.stream) 
print(b.stream)  
print(a.roll)   
  
# Class variables can be accessed using class
# name also
print(CSStudent.stream) 

#Python to implement getter and setter:
class CSStudent:
     
    # Class Variable
    stream = 'cse'     
     
    # The init method or constructor
    def __init__(self, roll):
         
        # Instance Variable
        self.roll = roll            
 
    # Adds an instance variable 
    def setAddress(self, address):
        self.address = address
     
    # Retrieves instance variable    
    def getAddress(self):    
        return self.address   
 
# Driver Code
a = CSStudent(101)
a.setAddress("Noida, UP")
print(a.getAddress()) 

