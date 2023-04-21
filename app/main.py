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
            Person.people[partner["name"]].wife\
                = Person.people[partner["wife"]]
        if partner.get("husband"):
            Person.people[partner["name"]].husband\
                = Person.people[partner["husband"]]
    return list_persons
