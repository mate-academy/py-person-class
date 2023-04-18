class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:
        person = Person(person["name"], person["age"])
        person_list.append(person)
    for partner in people:
        if partner.get("wife"):
            Person.people[partner["name"]].wife =\
                Person.people[partner["wife"]]
        elif partner.get("husband"):
            Person.people[partner["name"]].husband =\
                Person.people[partner["husband"]]

    return person_list
