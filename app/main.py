class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person['name'], person['age']) for person in people]

    for personage in people:
        if 'wife' in personage and personage['wife']:
            wife = Person.people[personage['wife']]
            Person.people[personage['name']].wife = wife
        elif 'husband' in personage and personage['husband']:
            husband = Person.people[personage['husband']]
            Person.people[personage['name']].husband = husband

    return persons
