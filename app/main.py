class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for sub in people:
        result.append(Person(sub["name"], sub["age"]))
    for sub in people:
        current = Person.people[sub["name"]]
        if "wife" in sub and sub["wife"] is not None:
            current.wife = Person.people[sub["wife"]]
        if "husband" in sub and sub["husband"] is not None:
            current.husband = Person.people[sub["husband"]]
    return result
