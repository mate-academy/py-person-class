class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    humans = [Person(name=human["name"], age=human["age"]) for human in people]
    for human in people:
        name = human["name"]
        if "wife" in human and human["wife"]:
            Person.people[name].wife = Person.people.get(human["wife"])
        if "husband" in human and human["husband"]:
            Person.people[name].husband = Person.people.get(human["husband"])
    return humans
