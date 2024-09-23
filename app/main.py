class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        if person.get("wife"):
            new_people[i].wife = Person.people[person["wife"]]
        if person.get("husband"):
            new_people[i].husband = Person.people[person["husband"]]

    return new_people
