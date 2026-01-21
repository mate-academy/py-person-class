class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list_obj = [Person(pers["name"], pers["age"]) for pers in people]
    for pers in people:
        if pers.get("wife"):
            wife = Person.people[pers["wife"]]
            Person.people[pers["name"]].wife = wife
        if pers.get("husband"):
            husband = Person.people[pers["husband"]]
            Person.people[pers["name"]].husband = husband
    return people_list_obj
