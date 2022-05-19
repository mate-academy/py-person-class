class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for human in people:
        for person in person_list:
            if person.name == human['name']:
                if 'wife' in human and human['wife'] is not None:
                    for wife in person_list:
                        if wife.name == human['wife']:
                            person.wife = wife
                if 'husband' in human and human['husband'] is not None:
                    for husband in person_list:
                        if husband.name == human['husband']:
                            person.husband = husband

    return person_list
