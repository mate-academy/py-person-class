class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objs = []
    for entry in people:
        person = Person(entry["name"], entry["age"])
        person_objs.append(person)

    for entry in people:
        person = Person.people[entry["name"]]
        if "wife" in entry and entry["wife"] is not None:
            person.wife = Person.people[entry["wife"]]
        if "husband" in entry and entry["husband"] is not None:
            person.husband = Person.people[entry["husband"]]

    return person_objs
