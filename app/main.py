class Person:
    people = {}


def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age
    Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = []
    Person.people = {}
    for person in people:
        name = person["name"]
        age = person["age"]
        persons.append(Person(name, age))

    for person, data in zip(persons, people):
        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]
        elif "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]
    return persons
