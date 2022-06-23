class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for people_x in people:
        person_list.append(Person(people_x['name'], people_x['age']))
    for people_x in people:
        if 'husband' in people_x and people_x['husband'] is not None:
            Person.people[people_x['name']].husband = \
                Person.people[people_x['husband']]
        if 'wife' in people_x and people_x['wife'] is not None:
            Person.people[people_x['name']].wife = \
                Person.people[people_x['wife']]
    return person_list
