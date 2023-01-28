class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife", None):
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife

        if person.get("husband", None):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return person_list
