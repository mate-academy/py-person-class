class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for i in people:
        instance = Person(i['name'], i['age'])
        person_instances.append(instance)
    for position, dict in enumerate(people):
        if 'wife' in dict and (dict['wife'] is not None):
            person_instances[position].wife = Person.people[dict['wife']]

        elif 'husband' in dict and dict['husband'] is not None:
            person_instances[position].husband = Person.people[dict['husband']]

    return person_instances
