class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self

    def __repr__(self):
        return f"{self.name, self.age}"


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband = (
                Person.people[human["husband"]]
            )

    return [human for human in Person.people.values()]
