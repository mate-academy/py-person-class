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

    for one_dict in people:
        if "wife" in one_dict and one_dict["wife"] is not None:
            Person.people[one_dict["name"]].wife =\
                Person.people[one_dict["wife"]]
        if "husband" in one_dict and one_dict["husband"] is not None:
            Person.people[one_dict["name"]].husband = \
                Person.people[one_dict["husband"]]
    return list_of_person
