class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person['name'], person['age'])
        person_list.append(new_person)

    for n in range(len(people)):
        if "husband" in people[n] and people[n]["husband"] is not None:
            for person in Person.people:
                if person == people[n]["name"]:
                    for spouse in Person.people:
                        if spouse == people[n]["husband"]:
                            Person.people[person].husband = \
                                Person.people[spouse]
        if "wife" in people[n] and people[n]["wife"] is not None:
            for person in Person.people:
                if person == people[n]["name"]:
                    for spouse in Person.people:
                        if spouse == people[n]["wife"]:
                            Person.people[person].wife = \
                                Person.people[spouse]

    return person_list
