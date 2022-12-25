class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"Person: {self.name}, age: {self.age}"

    def __repr__(self) -> str:
        return f"Person: {self.name}"


def create_person_list(people: list) -> list:
    humans_list = []
    for human in people:
        person = Person(name=human["name"], age=human["age"])
        humans_list.append(person)

    for i, human in enumerate(people):
        if "wife" in human.keys() and human["wife"] is not None:
            humans_list[i].wife = Person.people[human["wife"]]
        elif "husband" in human.keys() and human["husband"] is not None:
            humans_list[i].husband = Person.people[human["husband"]]
    return humans_list
