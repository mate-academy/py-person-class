class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for peop in people:
        person = Person(peop["name"], peop["age"])
        person_list.append(person)
    for peop in people:
        person = Person.people[peop["name"]]
        if "wife" in peop and peop["wife"] is not None:
            person.wife = Person.people[peop["wife"]]
        if "husband" in peop and peop["husband"] is not None:
            person.husband = Person.people[peop["husband"]]
    return person_list
