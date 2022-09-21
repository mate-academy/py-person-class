class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(peoples: list) -> list:
    person_list = [Person(name=pers["name"], age=pers["age"]) for pers in peoples]
    for pers in peoples:
        if pers.get("wife"):
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]

        if pers.get("husband"):
            Person.people[pers["name"]].husband = Person.people[pers["husband"]]

    return person_list
