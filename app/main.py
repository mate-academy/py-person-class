class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]
    return [Person.people[person["name"]] for person in people]
