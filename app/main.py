class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_humans = []

    for person in people:
        new_person = Person(person['name'], person['age'])
        list_of_humans.append(new_person)

    for index, human in enumerate(people):
        if 'wife' in human:
            if human['wife'] is not None:
                list_of_humans[index].wife = Person.people[human['wife']]
        if 'husband' in human:
            if human['husband'] is not None:
                list_of_humans[index].husband = Person.people[human['husband']]

    return list_of_humans
