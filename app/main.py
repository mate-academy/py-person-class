class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for i, human in enumerate(people):
        if 'wife' in human and human['wife'] is not None:
            for wife in person_list:
                if wife.name == human['wife']:
                    person_list[i].wife = wife
        if 'husband' in human and human['husband'] is not None:
            for husband in person_list:
                if husband.name == human['husband']:
                    person_list[i].husband = husband

    return person_list
