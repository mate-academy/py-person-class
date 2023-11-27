class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person(human["name"], human["age"]).wife = human["wife"]
        elif "husband" in human and human["husband"] is not None:
            Person(human["name"], human["age"]).husband = human["husband"]
        else:
            Person(human["name"], human["age"])

    for name, person in Person.people.items():
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return [person for person in Person.people.values()]
