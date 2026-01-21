class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        person_object = Person(human["name"], human["age"])
        person_list.append(person_object)

    for person in people:
        person_object = Person.people[person["name"]]

        if ("wife" in person) and (person["wife"] is not None):
            person_object.wife = Person.people[person["wife"]]
        elif ("husband" in person) and (person["husband"] is not None):
            person_object.husband = Person.people[person["husband"]]

    return person_list
