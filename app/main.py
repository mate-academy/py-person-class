class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=human["name"], age=human["age"]) for human in people
    ]

    for human in people:
        if human.get("wife") is not None:
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife

        if human.get("husband") is not None:
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband

    return person_list
