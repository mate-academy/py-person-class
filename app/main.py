class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        person = Person(human['name'], human['age'])
        if 'wife' in human and human['wife'] is not None:
            person.wife = human['wife']
        if 'husband' in human and human['husband'] is not None:
            person.husband = human['husband']
        result.append(person)
    for person in result:
        if hasattr(person, 'wife'):
            person.wife = Person.people[person.wife]
        if hasattr(person, 'husband'):
            person.husband = Person.people[person.husband]
    return result
