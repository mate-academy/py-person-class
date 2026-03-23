class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: create all Person instances
    instances = []
    for p in people:
        instances.append(Person(p["name"], p["age"]))

    # Second pass: link spouses
    for p, instance in zip(people, instances):
        if "wife" in p and p["wife"] is not None:
            instance.wife = Person.people[p["wife"]]
        elif "husband" in p and p["husband"] is not None:
            instance.husband = Person.people[p["husband"]]

    return instances