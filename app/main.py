class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people if person.get("name") is not None and person.get("age") is not None
    ]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return person_list
