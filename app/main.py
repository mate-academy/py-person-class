class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        instance = Person(name=person["name"], age=person["age"])
        instances.append(instance)

    for person in people:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]

    return instances
