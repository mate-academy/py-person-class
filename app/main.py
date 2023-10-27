class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_instances(people: list) -> None:
    for human in people:
        globals()[human["name"]] = Person(human["name"], human["age"])


def create_person_list(people: list) -> list:
    create_instances(people)
    person_instances = []
    for human in people:
        person_instances.append(Person.people[human["name"]])
        for key in human:
            if key == "wife" and human["wife"] is not None:
                person_instances[-1].wife = Person.people[human["wife"]]
            elif key == "husband" and human["husband"] is not None:
                person_instances[-1].husband = Person.people[human["husband"]]
    return person_instances
