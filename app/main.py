class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for i in people:
        new_list.append(Person(i['name'], i['age']))

    for x in people:
        if 'wife' in x and x['wife'] is not None:
            Person.people[x['name']].wife = Person.people[x['wife']]
        if 'husband' in x.keys():
            if x['husband'] is not None:
                Person.people[x['name']].husband = Person.people[x['husband']]
    return new_list
