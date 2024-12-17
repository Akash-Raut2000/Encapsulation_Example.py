class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):  # Getter
        return self.__name

    def set_name(self, name):  # Setter
        self.__name = name

# Usage
p = Person("Alice")
print(p.get_name())  # Output: Alice
p.set_name("Bob")
print(p.get_name())  # Output: Bob
