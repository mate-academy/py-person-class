class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for person in people:
        new_list.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                Person.people[person["name"]].wife = (
                    Person.people[person["wife"]]
                )
                Person.people[person["wife"]].husband = (
                    Person.people[person["name"]]
                )
    return new_list
