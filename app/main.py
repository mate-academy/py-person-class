class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instance_list = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        human_name = human["name"]
        if human.get("wife") is not None:
            Person.people[human_name].wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            Person.people[human_name].husband = Person.people[human["husband"]]

    return instance_list
