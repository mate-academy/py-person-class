class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_inst = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_inst.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person_inst.husband = Person.people[person["husband"]]

    return list(Person.people.values())
