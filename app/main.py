class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    update_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            if person["wife"] in Person.people:
                update_list[people.index(person)].wife = \
                    Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            if person["husband"] in Person.people:
                update_list[people.index(person)].husband = \
                    Person.people[person["husband"]]
    return update_list
