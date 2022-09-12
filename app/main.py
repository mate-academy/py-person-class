class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person['name'], person['age']) for person in people]

    for person in people:
        if 'wife' in person and person['wife']:
            husband = Person.people[person['name']]
            husband.wife = Person.people[person['wife']]
        elif 'husband' in person.keys() and person['husband']:
            wife = Person.people[person['name']]
            wife.husband = Person.people[person['husband']]

    return person_list
