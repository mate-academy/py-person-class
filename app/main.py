class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for el in range(len(result)):
        if 'wife' in people[el] and people[el]['wife'] is not None:
            result[el].wife = Person.people[people[el]['wife']]

        if 'husband' in people[el] and people[el]['husband'] is not None:
            result[el].husband = Person.people[people[el]['husband']]
    return result
