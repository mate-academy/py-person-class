class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            people_list[i].wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"] is not None:
            people_list[i].husband = Person.people.get(person["husband"])
    return people_list
