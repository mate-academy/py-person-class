class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "wife" in person and person["wife"]:
            w = Person.people[person["wife"]]
            Person.people[person["name"]].wife = w
        elif "husband" in person and person["husband"]:
            h = Person.people[person["husband"]]
            Person.people[person["name"]].husband = h

    return person_list
