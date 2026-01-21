class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for human in people:
        name = human["name"]
        if "wife" in human:
            if human["wife"] is not None:
                Person.people[name].wife = Person.people[human["wife"]]
        if "husband" in human:
            if human["husband"] is not None:
                Person.people[name].husband = Person.people[human["husband"]]

    return person_list
