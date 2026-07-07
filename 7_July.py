# class Animal :
#     def __init__(self,name):
#         self.name = name
#         print("hello ", self.name)
# class Dog(Animal):
#     def __init__(self,name):
#         super().__init__(name)
#         print("bark",self.name)
# Dog("Rocky") 

class Animal :
    def __init__(self,name):
        self.name = name
        print("Animal => ")
    def speak(self):
        print(f"Animal sound")            
class Dog(Animal) :
    def __init__(self,name):
        super().__init__(name)
        print("Dog => ")
    def speak(self):
        super().speak()
        print(f"{self.name} is barking")
class GoldenRetriever(Dog) :
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        super().speak()
        print(f"Golden Retriever barks happily")
d = GoldenRetriever("Rocky")
print(d.name)
d.speak()