class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_objects = []
    for p in people:
        person_objects.append(Person(p["name"], p["age"]))

    for p in people:
        person_instance = Person.people[p["name"]]

        if "wife" in p and p["wife"] is not None:
            setattr(person_instance, "wife", Person.people[p["wife"]])

        if "husband" in p and p["husband"] is not None:
            setattr(person_instance, "husband", Person.people[p["husband"]])

    return person_objects
