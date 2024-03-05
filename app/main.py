class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self.wife = None
        self.husband = None

    def __repr__(self):
        return f"{self.name}"


def create_person_list(people: list) -> list:
    # write your code here
    pass
