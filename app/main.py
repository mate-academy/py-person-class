class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    final_list = [Person(person['name'], person['age']) for person in people]

    for man in people:
        if man.get('wife'):
            Person.people[man['name']].wife = Person.people[man['wife']]
        if man.get('husband'):
            Person.people[man['name']].husband = Person.people[man['husband']]
    return final_list
