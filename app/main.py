class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person['name'], person['age']) for person in people]

    for i, person in enumerate(people):
        if person.get('wife'):
            result[i].wife = result[i].people[person['wife']]
        if person.get('husband'):
            result[i].husband = result[i].people[person['husband']]

    return result






