class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: create all Person instances
    person_list = []
    for entry in people:
        person = Person(entry["name"], entry["age"])
        person_list.append(person)

    # Second pass: link spouses
    for entry in people:
        person = Person.people[entry["name"]]
        if "wife" in entry and entry["wife"] is not None:
            person.wife = Person.people[entry["wife"]]
        elif "husband" in entry and entry["husband"] is not None:
            person.husband = Person.people[entry["husband"]]

    return person_list
