class Person:
    people = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))
    for couple in people:
        if "wife" in couple and couple["wife"] is not None:
            Person.people[couple["name"]].wife = Person.people[couple["wife"]]
        if "husband" in couple and couple["husband"] is not None:
            Person.people[couple["name"]].husband =\
                (Person.people[couple["husband"]])

    return people_list
