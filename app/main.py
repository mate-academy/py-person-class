class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    instances = []
    for person in people:
        instances.append(Person(person["name"], person["age"]))
    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]
    return instances
