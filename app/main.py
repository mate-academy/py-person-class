class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])

    for person in people:
        if 'husband' in person and person['husband'] is not None:
            Person.people[person["name"]].husband = Person.people[person["husband"]]

        if 'wife' in person and person['wife'] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

    return [person for person in Person.people.values()]
