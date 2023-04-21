class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_persons = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]
    for partner in people:
        if partner.get("wife"):
            wife = Person.people[partner["wife"]]
            wife.husband = Person.people[partner["name"]]
        if partner.get("husband"):
            husband = Person.people[partner["husband"]]
            husband.wife = Person.people[partner["name"]]
    return list_persons
