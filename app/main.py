class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        result_list.append(new_person)

    for person in people:
        current = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            current.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            current.husband = Person.people[person["husband"]]

    return result_list
