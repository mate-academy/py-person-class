class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    friends = []
    for person in people:
        friends.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                Person.people[person["name"]].husband = Person.people[person["husband"]]
    return friends