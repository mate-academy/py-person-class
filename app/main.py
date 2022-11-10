class Person:
    people = {}

    def __init__(self, name: str, age: int) -> callable:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for dict_person in people:
        person_list.append(Person(dict_person["name"], dict_person["age"]))
    for dict_person in people:
        if "wife" in dict_person and dict_person["wife"] is not None:
            Person.people[dict_person["name"]].wife \
                = Person.people[dict_person["wife"]]
        if "husband" in dict_person and dict_person["husband"] is not None:
            Person.people[dict_person["name"]].husband \
                = Person.people[dict_person["husband"]]
    return person_list
