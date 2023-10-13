class Person:
    people = {}

    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
