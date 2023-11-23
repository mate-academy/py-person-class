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
        wife_name = human.get("wife")
        if wife_name in Person.people:
            Person.people[name].wife = Person.people[wife_name]
    for human in people:
        name = human["name"]
        husband_name = human.get("husband")
        if husband_name in Person.people:
            Person.people[name].husband = Person.people[husband_name]
    return inst_list
