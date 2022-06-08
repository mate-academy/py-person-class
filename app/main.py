class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    lst = [Person(obj['name'], obj['age']) for obj in people]

    for i, obj in enumerate(people):
        if "wife" in obj and obj["wife"] is not None:
            lst[i].wife = Person.people[obj["wife"]]
        if "husband" in obj and obj["husband"] is not None:
            lst[i].husband = Person.people[obj["husband"]]
    return lst
