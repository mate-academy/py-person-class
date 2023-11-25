class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i, person in enumerate(people):
        if "wife" in person:
            if person["wife"] in Person.people:
                person_list[i].wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] in Person.people:
                person_list[i].husband = Person.people[person["husband"]]

    return person_list
