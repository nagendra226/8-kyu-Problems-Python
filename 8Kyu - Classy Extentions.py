class Cat(Animal):
    #your code here
    def __init__(self,name):
        self.name = name
    def speak(self):
        return '{} meows.'.format(self.name)
