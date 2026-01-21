class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for individual in people:
        Person(individual['name'], individual['age'])
    for individual in people:
        new_ind = Person.people[individual['name']]
        if 'husband' in individual and individual['husband']:
            new_ind.husband = Person.people[individual['husband']]
        elif 'wife' in individual and individual['wife']:
            new_ind.wife = Person.people[individual['wife']]
        result_list.append(new_ind)
    return result_list
