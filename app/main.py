class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for per in people:
        person = Person(per["name"], per["age"])
        person_list.append(person)

    for per in people:
        person = Person.people[per["name"]]
        if "wife" in per and per["wife"] is not None:
            person.wife = Person.people[per["wife"]]
        elif "husband" in per and per["husband"] is not None:
            person.husband = Person.people[per["husband"]]

    return person_list
