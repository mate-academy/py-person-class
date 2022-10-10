class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    list_person = []
    for one_person in people:
        person = Person(one_person["name"],
                        one_person["age"])
        list_person.append(person)

    for wife_husband in people:
        if "wife" in wife_husband and wife_husband["wife"] is not None:
            Person.people[wife_husband["name"]].wife \
                = Person.people[wife_husband["wife"]]

        elif "husband" in wife_husband and wife_husband["husband"] is not None:
            Person.people[wife_husband["name"]].husband \
                = Person.people[wife_husband["husband"]]

    return list_person
