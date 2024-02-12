class Stringtask1:
    def getString(self) :
        self.string = input("Enter a string please")

    def printString(self) :
        print("String in uppercase:", self.string.upper())

task1 = Stringtask1()
task1.getString()
task1.printString()