class print1:
    def __init__(self, name):
        self.name = name
    def print(self):
        print(self.name)

class print2:
    def __init__(self, name):
        self.name = name
    def print(self):
        print(self.name)

print1("print1").print()
print2("print2").print()
