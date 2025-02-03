class StringProcessor:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Joldy engz: ")
    
    def printString(self):
        print(self.text.upper())

processor = StringProcessor()
processor.getString()
processor.printString()