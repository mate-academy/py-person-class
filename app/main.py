class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for per in people:
        Person(per["name"], per["age"])

    for per in people:
        if "wife" in per and per["wife"]:
            Person.people[per["name"]].wife = Person.people[per["wife"]]
        if "husband" in per and per["husband"]:
            Person.people[per["name"]].husband = Person.people[per["husband"]]

    return list(Person.people.values())
