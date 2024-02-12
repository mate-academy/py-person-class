class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self. age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    result = [
        Person(human["name"], human["age"])
        for human in people
    ]

    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
            Person.people[human["wife"]].husband = Person.people[human["name"]]
    return result
