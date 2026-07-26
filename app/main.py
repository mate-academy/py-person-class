class Person:
    people = []
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

    pass


def create_person_list(people: list) -> list:
    return [Person(name, age) for name, age in people]
    pass
