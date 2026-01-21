class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for husband in people:
        if "wife" in husband and husband["wife"]:
            Person.people[husband["name"]].wife = (
                Person.people[husband["wife"]]
            )
            Person.people[husband["wife"]].husband = (
                Person.people[husband["name"]]
            )

    return person_list
