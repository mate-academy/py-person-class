class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person["name"], person["age"]) for person in people]
    for pers in people:
        inst = Person.people[pers["name"]]
        wife = pers.get("wife")
        if wife is not None:
            inst.wife = Person.people[wife]
        husband = pers.get("husband")
        if husband is not None:
            inst.husband = Person.people[husband]

    return person_list
