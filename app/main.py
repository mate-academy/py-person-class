class Person:
    people = {}

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]
    for per in people:
        if "wife" in per and per["wife"] in Person.people:
            Person.people[per["wife"]].husband = Person.people[per["name"]]
        elif "husband" in per and per["husband"] in Person.people:
            Person.people[per["husband"]].wife = Person.people[per["name"]]

    return person_list
