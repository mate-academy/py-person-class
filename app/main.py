class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(person['name'], person['age']) for person in people]

    for i, person in enumerate(people):
        if person.get('wife'):
            instances[i].wife = instances[i].people[person['wife']]
        if person.get('husband'):
            instances[i].husband = instances[i].people[person['husband']]

    return instances
