class Person:
    people = {}

    def __init__(self, name: str, age: int) -> callable:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for i in people:
        person_list.append(Person(i["name"], i["age"]))
    for i in people:
        if "wife" in i and i["wife"] is not None:
            Person.people[i["name"]].wife = Person.people[i["wife"]]
        if "husband" in i and i["husband"] is not None:
            Person.people[i["name"]].husband = Person.people[i["husband"]]
    return person_list
