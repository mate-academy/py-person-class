class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person['name'], person['age']))
    for key in Person.people.keys():
        for person in people:
            if key == person['name']:
                if 'wife' in person and person['wife'] is not None:
                    Person.people[key].wife = Person.people[person['wife']]
                elif 'husband' in person and person['husband'] is not None:
                    Person.people[key].husband \
                        = Person.people[person['husband']]
                else:
                    pass
            else:
                pass
    return person_list
