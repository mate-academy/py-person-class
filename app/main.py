class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        current = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            current.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"]:
            current.husband = Person.people[person["husband"]]

    return person_list
