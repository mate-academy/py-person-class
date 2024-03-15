class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "wife" in person:
            if not person["wife"] is None:
                Person.people[person["name"]].wife \
                    = Person.people[person["wife"]]
                Person.people[person["wife"]].husband \
                    = Person.people[person["name"]]

    return people_list
