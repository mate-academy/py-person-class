class Person:

    people = {}

    def __init__(self, name: str, age: int, ):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons_list = []
    for person in people:
        persons_list.append(Person(person['name'], person['age']))

    for peopl in people:
        if 'wife' in peopl:
            if peopl['wife'] is not None:
                Person.people[peopl['name']].wife = \
                    Person.people[peopl['wife']]

        if 'husband' in peopl:
            if peopl['husband'] is not None:
                Person.people[peopl['name']].husband = \
                    Person.people[peopl['husband']]

    return persons_list
