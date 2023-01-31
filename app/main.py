class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list) -> list:
    person_array = []
    for person in persons:
        person_array.append(Person(name=person["name"], age=person["age"]))
    for person in persons:
        if "wife" in person.keys() and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person.keys() and person["husband"] is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]
    return person_array
