class Person:
    people = {}
    def __init__ (self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person['name'], person['age']) for human in people]

    for person in result:
        if 'wife' in person and person['wife'] is not None:
            person.wife = Person.people[person['wife']]
        if 'husband' in person and person['husband'] is not None:
            person.husband = Person.people[person['husband']]

    return result
