class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people):
    person_instances = []
    for person_dict in people:
        person = Person(person_dict['name'], person_dict['age'])
        if 'wife' in person_dict and person_dict['wife'] is not None:
            person.wife = Person.people[person_dict['wife']]
        if 'husband' in person_dict and person_dict['husband'] is not None:
            person.husband = Person.people[person_dict['husband']]
        person_instances.append(person)
    return person_instances
