class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for i, person in enumerate(people):
        if "husband" in person and person["husband"] is not None:
            result[i].husband = Person.people[person['husband']]

        if "wife" in person and person["wife"] is not None:
            result[i].wife = Person.people[person['wife']]

    return result
