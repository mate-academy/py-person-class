class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for one in people:
        Person(one["name"], one["age"])

    for one in people:
        if "wife" in one and one["wife"] is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]

        elif "husband" in one and one["husband"] is not None:
            Person.people[one["name"]].husband = Person.people[one["husband"]]

    return list(Person.people.values())
