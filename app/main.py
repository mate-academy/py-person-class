class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = []

    for one_dict in people:
        list_of_person.append(Person(one_dict["name"], one_dict["age"]))

    for person_dict in people:
        if "wife" in person_dict and person_dict["wife"] is not None:
            Person.people[person_dict["name"]].wife =\
                Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            Person.people[person_dict["name"]].husband = \
                Person.people[person_dict["husband"]]
    return list_of_person
