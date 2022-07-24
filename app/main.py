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

    for item in people:
        person_list.append(Person(item["name"], item["age"]))

    for item in people:
        name = item["name"]

        wife = item["wife"] if "wife" in item else None
        if wife:
            Person.people[name].wife = Person.people[wife]

        husband = item["husband"] if "husband" in item else None
        if husband:
            Person.people[name].husband = Person.people[husband]

    return person_list
