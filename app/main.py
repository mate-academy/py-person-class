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

    for one_person in people:
        if one_person.get("wife"):
            Person.people[one_person["name"]].wife = \
                Person.people[one_person["wife"]]
        if one_person.get("husband"):
            Person.people[one_person["name"]].husband = \
                Person.people[one_person["husband"]]

    return person_list
