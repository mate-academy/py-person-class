class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for human in people:
        human_person = Person(human['name'], human['age'])
        result.append(human_person)

    for i in range(len(result)):

        if 'wife' in people[i] and people[i]['wife'] is not None:
            result[i].wife = Person.people[people[i]['wife']]

        elif 'husband' in people[i] and people[i]['husband'] is not None:
            result[i].husband = Person.people[people[i]['husband']]

    return result
