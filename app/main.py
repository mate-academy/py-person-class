class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for i, person in enumerate(people):
        person_list.append(Person(name=person['name'], age=person['age']))

    for i, person in enumerate(people):
        if 'wife' in person and person['wife']:
            person_list[i].wife = Person.people[person['wife']]

        if 'husband' in person and person['husband']:
            person_list[i].husband = Person.people[person['husband']]

    return person_list
