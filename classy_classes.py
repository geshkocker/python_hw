class Person():
    def __init__(self,name,age):
        self.__information =f"{name}s age is {age}"
        
    @property
    def info(self):
        return self.__information