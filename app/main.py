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

    for i in range(len(result)):
        if "husband" in people[i] and people[i]["husband"] is not None:
            result[i].husband = Person.people[people[i]['husband']]

        if "wife" in people[i] and people[i]["wife"] is not None:
            result[i].wife = Person.people[people[i]['wife']]

    return result
