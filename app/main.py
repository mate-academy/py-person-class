class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        result.append(Person(name, age))
    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                current = Person.people[person["name"]]
                current.wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                current = Person.people[person["name"]]
                current.husband = Person.people[person["husband"]]

    return result
