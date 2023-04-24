# update progress
class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(peoples: list) -> list:
    list_with_person = [Person(person["name"], person["age"])
                        for person in peoples]

    for person in peoples:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return list_with_person
