class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    persons = []
    for person in peoples:
        persons.append(Person(person['name'], person['age']))

    for people in peoples:
        if 'wife' in people and people['wife'] is not None:
            wife = Person.people[people['wife']]
            Person.people[people['name']].wife = wife
        if 'husband' in people and people['husband'] is not None:
            husband = Person.people[people['husband']]
            Person.people[people['name']].husband = husband

    return persons
