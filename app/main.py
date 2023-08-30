class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[name] = (self)

def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person, man in zip(persons, people):
        if "wife" in man and man["wife"]:
            for peop in Person.people:
                if peop == man["wife"]:
                    person.wife = Person.people[peop]
        if "husband" in man and man["husband"]:
            for peop in Person.people:
                if peop == man["husband"]:
                    person.husband = Person.people[peop]
    return persons
