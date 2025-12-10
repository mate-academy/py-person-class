class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    pupil_array = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]

        elif person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return pupil_array
