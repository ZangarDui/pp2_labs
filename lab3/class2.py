class Shape:  
    def __init__(self):
        pass  
    
    def area(self):  
        return 0  

class Square(Shape):  
    def __init__(self, length):  
        self.length = length  

    def area(self):  
        return self.length ** 2  


shape = Shape()  
square = Square(5)  

print("Shape аумағы:", shape.area())  
print("Square аумағы:", square.area())