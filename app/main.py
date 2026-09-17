class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(pers["name"], pers["age"]) for pers in people]

    for pers in people:
        person_instance = Person.people[pers["name"]]
        if pers.get("wife"):
            person_instance.wife = Person.people[pers["wife"]]
        if pers.get("husband"):
            person_instance.husband = Person.people[pers["husband"]]
    return result_list
