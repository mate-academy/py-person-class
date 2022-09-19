class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if "husband" in person:
            if person["husband"] in Person.people:
                Person.people[person["name"]].husband \
                    = Person.people[person["husband"]]

        if "wife" in person:
            if person["wife"] in Person.people:
                Person.people[person["name"]].wife\
                    = Person.people[person["wife"]]

    return list(Person.people.values())
