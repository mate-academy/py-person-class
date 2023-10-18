class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        persons.append(Person(person["name"], person["age"]))
    for i, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            persons[i].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            persons[i].husband = Person.people[person["husband"]]
    return persons
