class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    humans = [Person(unit["name"], unit["age"]) for unit in people]
    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        elif person.get("husband") is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return humans
