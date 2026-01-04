"""
Instance Fields: These are fields tied to a specific instance of a class.
实例字段：这些字段与类的特定实例相关。
Class Fields: These are fields shared by all instances of a class.
类字段：这些字段由类的所有实例共享。
"""


class Person:
    high = "180"  # Class fields

    def __init__(self, name, age):
        self.name = name  # instance field
        self.age = age


def main():
    person1 = Person("Alice", 18)
    person2 = Person("Bob", 25)

    Person.high = "200"
    print(f"Person.high = {Person.high}")  # Class fields, if change it , all instances will be changed.

    print(f"person1.name = {person1.name}")
    print(f"person1.high = {person1.high}")

    print(f"person2.age = {person2.age}")
    print(f"person2.high = {person2.high}")


if __name__ == "__main__":
    main()
