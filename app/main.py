class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        instance = Person(person["name"], person["age"])
        person_list.append(instance)

    for i, person in enumerate(people):
        if "wife" in person.keys() and person["wife"] is not None:
            person_list[i].wife = Person.people[person["wife"]]
        if "husband" in person.keys() and person["husband"] is not None:
            person_list[i].husband = Person.people[person["husband"]]

    return person_list
