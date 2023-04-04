class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    result = [Person(human.get("name"), human.get("age")) for human in people]

    for human in people:
        human_ = Person.people.get(human["name"])
        if human.get("wife"):
            human_.wife = Person.people[human["wife"]]
        if human.get("husband"):
            human_.husband = Person.people[human["husband"]]
    return result
