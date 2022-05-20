class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person['name'], person['age']) for person in people]

    for people in people:
        if 'wife' in people and people['wife']:
            wife = Person.people[people['wife']]
            Person.people[people['name']].wife = wife
        if 'husband' in people and people['husband']:
            husband = Person.people[people['husband']]
            Person.people[people['name']].husband = husband

    return persons
