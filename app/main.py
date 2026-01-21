class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        if "wife" in person and person["wife"] in Person.people:
            person_list[index].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] in Person.people:
            person_list[index].husband = Person.people[person["husband"]]

    return person_list
