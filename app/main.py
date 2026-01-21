class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = [Person(pers["name"], pers["age"]) for pers in people]
    for pers in people:
        if pers.get("wife"):
            husband = Person.people[pers["name"]]
            husband.wife = Person.people[pers["wife"]]

        if pers.get("husband"):
            wife = Person.people[pers["name"]]
            wife.husband = Person.people[pers["husband"]]

    return person_list
