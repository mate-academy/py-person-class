class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    lis = []
    for person in people:
        user = Person(person["name"], person["age"])
        lis.append(user)
    for per in people:
        if "wife" in per and per["wife"] is not None:
            Person.people[per["name"]].wife = Person.people[per["wife"]]
        if "husband" in per and per["husband"] is not None:
            Person.people[per["name"]].husband = Person.people[per["husband"]]
    return lis
