class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    res = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for i in range(len(res)):
        if 'husband' in people[i] and people[i]['husband'] is not None:
            res[i].husband = Person.people[people[i]['husband']]

        if 'wife' in people[i] and people[i]['wife'] is not None:
            res[i].wife = Person.people[people[i]['wife']]

    return res
