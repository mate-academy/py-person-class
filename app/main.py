class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    person_list = [Person.people[person["name"]] for person in people]
    for i, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            person_list[i].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person_list[i].husband = Person.people[person["husband"]]
    return person_list
