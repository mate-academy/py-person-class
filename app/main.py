class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        persons_list.append(new_person)

    for person in people:
        new_person = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            new_person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            new_person.husband = Person.people[person["husband"]]
    return persons_list
