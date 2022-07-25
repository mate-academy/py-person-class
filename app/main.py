class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.store_person(self, name)

    @classmethod
    def store_person(cls, self, name):
        cls.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        name = person["name"]

        wife = person["wife"] if "wife" in person else None
        if wife:
            Person.people[name].wife = Person.people[wife]

        husband = person["husband"] if "husband" in person else None
        if husband:
            Person.people[name].husband = Person.people[husband]

    return person_list
