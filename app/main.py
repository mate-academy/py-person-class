class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person["name"], person["age"]) for person in people
    ]

    for ind in people:
        """ind -> individual ;P; in other case the line"s too long"""
        if ind.get("wife"):
            Person.people[ind["name"]].wife = Person.people[ind["wife"]]
        elif ind.get("husband"):
            Person.people[ind["name"]].husband = Person.people[ind["husband"]]

    return person_instances
