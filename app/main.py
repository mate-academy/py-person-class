class Person:
    person = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.person[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    return person_list[]
