class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(human["name"], human["age"]) for human in people]

    for person in people:

        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        elif person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return people_list
