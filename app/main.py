class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        one_of_marrieds = Person.people[person["name"]]
        if "wife" in person and person["wife"] in Person.people:
            one_of_marrieds.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] in Person.people:
            one_of_marrieds.husband = Person.people[person["husband"]]

    return list(Person.people.values())
