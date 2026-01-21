class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person in people:
        if person.get('wife') is not None:
            Person.people[person['name']].wife = Person.people[person['wife']]
        elif person.get('husband') is not None:
            Person.people[person['name']].husband =\
                Person.people[person['husband']]
    return persons
