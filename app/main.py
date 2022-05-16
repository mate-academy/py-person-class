class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def create_person_list(people: list) -> list:
        person_list = []
        for n in Person.people:
            p = Person(n['name'], n['age'])
            if n['wife'] is not None:
                for h in Person.people:
                    if h['husband'] == n['name']:
                        p.wife = h
            if n['husband'] is not None:
                for h in Person.people:
                    if h['wife'] == n['name']:
                        p.husband = h
            person_list.append(p)