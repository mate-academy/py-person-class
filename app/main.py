class Person:
    people = {}

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]
    for human in people:
        if "wife" in human and human["wife"] in Person.people:
            # husband_wife = Person.people[person["wife"]]
            # name = Person.people[person["name"]]
            # husband_wife.husband = name
            Person.people[human["wife"]].husband = Person.people[human["name"]]
        elif "husband" in human and human["husband"] in Person.people:
            # husband_wife = Person.people[person["husband"]]
            # husband_wife.wife = name
            Person.people[human["husband"]].wife = Person.people[human["name"]]

    return person_list
