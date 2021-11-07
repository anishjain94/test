class MyClass:
    def method(self):
        print(self.__class__)

    @classmethod
    def classmethod(cls):
        print( 'class method called', cls)

    @staticmethod
    def staticmethod():
        print( 'static method called')

obj = MyClass()
obj.method()
# MyClass.method(obj)
obj.classmethod()
