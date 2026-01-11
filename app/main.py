class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [Person(p['name'], p['age']) for p in people]

    for p in people:
        instance = Person.people[p['name']]

        if p.get('wife') is not None:
            instance.wife = Person.people[p['wife']]

        if p.get('husband') is not None:
            instance.husband = Person.people[p['husband']]

    return person_list