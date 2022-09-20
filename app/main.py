class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif "husband" in human and \
                human["husband"] is not None:
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]
    return new_list
