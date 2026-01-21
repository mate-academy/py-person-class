class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    persons = [Person(pers["name"], pers["age"]) for pers in people]
    for pers in people:
        obj = Person.people[pers["name"]]
        if pers.get("wife"):
            obj.wife = Person.people[pers["wife"]]
        if pers.get("husband"):
            obj.husband = Person.people[pers["husband"]]

    return persons
