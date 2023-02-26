class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        person = Person(person["name"], person["age"])
        result.append(person)
    for partner in people:
        name = partner["name"]
        if partner.get("wife"):
            Person.people[name].wife = Person.people[partner["wife"]]
        elif partner.get("husband"):
            Person.people[name].husband = Person.people[partner["husband"]]
    return result
