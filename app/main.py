class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for p in people:
        if "wife" in p:
            if p["wife"] is not None:
                Person.people[p["name"]].wife = Person.people[p["wife"]]
        if "husband" in p:
            if p["husband"] is not None:
                Person.people[p["name"]].husband = Person.people[p["husband"]]
    return person_list
