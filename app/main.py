class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self. age = age
        __class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_person in people:
        person_list.append(Person(one_person["name"], one_person["age"]))
    for index, first_person in enumerate(people):
        if "wife" in first_person and first_person["wife"] is not None:
            person_list[index].wife = Person.people[first_person['wife']]
        if "husband" in first_person and first_person["husband"] is not None:
            person_list[index].husband =\
                Person.people[f"{first_person['husband']}"]
    return person_list
