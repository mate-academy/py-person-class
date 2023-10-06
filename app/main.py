class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for spouse in people:
        if spouse.get("wife"):
            Person.people[spouse["name"]].wife = Person.people[spouse["wife"]]
        elif spouse.get("husband"):
            Person.people[spouse["name"]].husband = (
                Person.people[spouse["husband"]]
            )

    return person_list
