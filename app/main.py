class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    list_of_persons = [Person(pers["name"], pers["age"]) for pers in people]

    for person in people:

        if "wife" in person and person["wife"] is not None:
            husband = Person.people[person["name"]]
            husband.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            wife = Person.people[person["name"]]
            wife.husband = Person.people[person["husband"]]

    return list_of_persons
