class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if human.get("husband"):
            Person.people[human["name"]].husband = (
                Person.people[human["husband"]]
            )
    return person_list
