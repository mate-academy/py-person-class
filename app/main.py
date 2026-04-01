class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for info in people:
        person = Person(info["name"], info["age"])
        result.append(person)

    for info in people:
        person = Person.people[info["name"]]

        if "wife" in info and info["wife"] is not None:
            person.wife = Person.people[info["wife"]]

        if "husband" in info and info["husband"] is not None:
            person.husband = Person.people[info["husband"]]

    return result
