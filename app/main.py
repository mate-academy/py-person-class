class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(one_person["name"], one_person["age"]) for one_person in people
    ]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return person_list
