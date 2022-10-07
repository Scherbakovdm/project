class Person:
    def __init__(self, name: str, surname: str, age: int) ->None:
        self.first_name = name
        self.last_name = surname
        self.age = age
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    def is_adult(self):
        return self.age >= 18


p1 = Person('Jimi', "Hendrix", age = 55)
print("ds")
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"