class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    inst_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        name = human["name"]
        if "wife" in human.keys():
            if human["wife"] in Person.people:
                Person.people[name].wife = Person.people[human["wife"]]
        if "husband" in human.keys():
            if human["husband"] in Person.people:
                Person.people[name].husband = Person.people[human["husband"]]
    return inst_list
