class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self

def create_person_list(people: list) -> list:
    persons =[]
    for person in people:
        Person(person['name'], person['age'])

    for person_dict, person_obj in zip(people, persons):
        spouse_name = person_dict.get('wife') or person_dict.get('husband')
        if spouse_name:
                if 'wife' in person_dict:
                    person_obj.wife = Person.people[spouse_name]
                else:
                    person_obj.husband = Person.people[spouse_name]

    return persons

