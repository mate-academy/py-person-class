class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    # Create list and populate it with newly created people.
    people_list = [Person(person_dict['name'], person_dict['age'])
                   for person_dict in people]

    # Iterate second time so that all people are created by now.
    for person_dict in people:
        person = Person.people[person_dict['name']]
        if wife := person_dict.get('wife'):
            person.wife = Person.people[wife]
        elif husband := person_dict.get('husband'):
            person.husband = Person.people[husband]

    return people_list
