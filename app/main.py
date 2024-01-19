class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    persons =[]
    for person in people:
        persons.append(Person(person['name'], person["age"]))

