class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for new_person in people:
        person_list.append(Person(new_person["name"], new_person["age"]))
    for new_person in people:
        if new_person.get("wife") is not None:
            Person.people[new_person["name"]].wife =\
                Person.people[new_person["wife"]]
        if new_person.get("husband") is not None:
            Person.people[new_person["name"]].husband =\
                Person.people[new_person["husband"]]
    return person_list
