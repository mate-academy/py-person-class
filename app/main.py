class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(person["name"], person["age"]) for person in people]

    for person, instance in zip(people, instances):
        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]

    return instances