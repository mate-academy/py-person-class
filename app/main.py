class Person:
    people = dict()

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list):
    list_of_person = [Person(pers["name"], pers["age"]) for pers in people]
    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]

    return list_of_person
