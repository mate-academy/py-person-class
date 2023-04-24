class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        human_name = Person.people[human["name"]]
        if human.get("wife") is not None:
            human_name.wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            human_name.husband = Person.people[human["husband"]]
    return person_list
