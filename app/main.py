class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])
    for human in people:
        if "wife" in human:
            if human["wife"] in Person.people:
                Person.people[human["name"]].wife = \
                    Person.people[human["wife"]]

        if "husband" in human:
            if human["husband"] in Person.people:
                Person.people[human["name"]].husband = \
                    Person.people[human["husband"]]

    return list(Person.people.values())
