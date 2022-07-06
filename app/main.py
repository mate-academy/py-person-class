class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    list_instances = []
    for dict_people in people:
        instance = Person(dict_people['name'], dict_people['age'])
        list_instances.append(instance)
    for position, dict in enumerate(people):
        if 'wife' in dict and (dict['wife'] is not None):
            list_instances[position].wife = Person.people[dict['wife']]

        elif 'husband' in dict and dict['husband'] is not None:
            list_instances[position].husband = Person.people[dict['husband']]

    return list_instances
