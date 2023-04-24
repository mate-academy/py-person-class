class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    info_people = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        current_object = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            current_object.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            current_object.husband = Person.people[person["husband"]]

    return info_people
