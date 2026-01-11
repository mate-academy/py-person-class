class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]

    for i, person in enumerate(people):
        current = people_list[i]
        if person.get("wife"):
            current.wife = Person.people[person["wife"]]

        elif person.get("husband"):
            current.husband = Person.people[person["husband"]]

    return people_list
