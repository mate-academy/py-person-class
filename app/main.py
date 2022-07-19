class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for human in people:
        if "wife" in human:
            if human["wife"] is not None:
                Person.people[human["name"]].wife = \
                    Person.people[human["wife"]]
        if "husband" in human:
            if human["husband"] is not None:
                Person.people[human["name"]].husband = \
                    Person.people[human["husband"]]
    return person_list
