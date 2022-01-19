class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    pupil_array = [Person(person["name"], person["age"]) for person in people]

    for persons in people:
        if persons.get("wife"):
            Person.people[persons["name"]].wife = \
                Person.people[persons["wife"]]

        elif persons.get("husband"):
            Person.people[persons["name"]].husband = \
                Person.people[persons["husband"]]

    return pupil_array
