class Person:
    people = {}

    def __init__(self, name: str, age: int) -> dict:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        individual = Person.people[person["name"]]
        if person.get("wife") and person["wife"] is not None:
            individual.__dict__["wife"] = Person.people[person["wife"]]
        if person.get("husband") and person["husband"] is not None:
            individual.__dict__["husband"] = Person.people[person["husband"]]
        person_list.append(Person.people[person["name"]])
    return person_list
