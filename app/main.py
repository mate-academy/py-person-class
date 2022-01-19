class Person:
    people = dict()

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list):
    ls = []
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]
        ls.append(Person.people[person["name"]])
    return ls
