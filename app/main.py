class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return [person for person in Person.people.values()]
