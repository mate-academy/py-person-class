class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    new_people = [
        Person(name=human["name"], age=human["age"])
        for human in people
    ]

    for index, human in enumerate(people):
        if human.get("wife"):
            new_people[index].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            new_people[index].husband = Person.people[human["husband"]]
    return new_people
