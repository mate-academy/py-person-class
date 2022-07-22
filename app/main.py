class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:
        instance = Person(person["name"], person["age"])
        person_list.append(instance)

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        elif "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]

    return person_list
