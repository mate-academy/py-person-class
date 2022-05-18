class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(peoples: list) -> list:
    resultList = [Person(person['name'], person['age']) for person in peoples]
    for person in peoples:
        if 'husband' in person and person['husband']:
            husband = Person.people[person['husband']]
            Person.people[person['name']].husband = husband

        if 'wife' in person and person['wife']:
            wife = Person.people[person['wife']]
            Person.people[person['name']].wife = wife

    return resultList
