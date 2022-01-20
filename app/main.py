class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    result = [Person(i['name'], i['age']) for i in people]
    for j in people:
        if 'wife' in j and j['wife'] is not None:
            Person.people[j['name']].wife = Person.people[j['wife']]
        elif 'husband' in j and j['husband'] is not None:
            Person.people[j['name']].husband = Person.people[j['husband']]
    return result
