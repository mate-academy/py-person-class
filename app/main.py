from ast import Str


class Person:
    people = {}

    def __init__(self, name, age) -> None:

        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self

    def create_person_list(self, people) -> list:

        person_list = []
        for human in people:
            person = Person(human['name'], human['age'])
            if human['wife'] is not None:
                person.wife = Person.people[human['wife']]
                Person.people[human['wife']].husband = person
            elif human['husband'] is not None:
                person.husband = Person.people[human['husband']]
                Person.people[human['husband']].wife = person
            person_list.append(person)
        return person_list
