class Person:
    people = dict()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list):
    person_list = []
    for person in people:
        person_list.append(Person(name=person['name'], age=person['age']))
    for person in people:
        if person.get('wife'):
            Person.people[person['name']].wife = Person.people[person['wife']]
        if person.get('husband'):
            husband = Person.people[person['husband']]
            Person.people[person['name']].husband = husband
    return person_list
