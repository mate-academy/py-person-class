class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for p in people:
        person = Person(p["name"], p["age"])
        result.append(person)

    for p in person:
        person = Person.people(p["name"])

        if "wife" in p and p["wife"] is not None:
            person.wife = Person.people[p["wife"]]

        if "husband" in p and p["husband"] is not None:
            person.husband = Person.people[p["husband"]]

    return result