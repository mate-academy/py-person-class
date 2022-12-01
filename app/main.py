class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_list = []
    for person in people:
        human = Person(person["name"], person["age"])
        instances_list.append(human)
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return instances_list
