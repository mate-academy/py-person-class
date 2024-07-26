class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:

        Person(name=person["name"], age=person["age"])

    for person in people:

        name = person["name"]

        if "wife" in person and person["wife"]:
            Person.people[name].wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"]:
            Person.people[name].husband = Person.people[person["husband"]]

    return [person for person in Person.people.values()]
