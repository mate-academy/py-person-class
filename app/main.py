class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_to_create: list) -> list:
    person_list = [Person(name=person["name"], age=person["age"])
                   for person in people_to_create]

    for person in people_to_create:
        if "wife" in person.keys() and person["wife"] is not None:
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        elif "husband" in person.keys() and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return person_list
