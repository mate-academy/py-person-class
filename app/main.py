class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for pep in people:
        new_list.append(Person(pep["name"], pep["age"]))
    for pep in people:
        if "wife" in pep and pep["wife"] is not None:
            Person.people[pep["name"]].wife = Person.people[pep["wife"]]
        if "husband" in pep and pep["husband"] is not None:
            Person.people[pep["name"]].husband = Person.people[pep["husband"]]
    return new_list
