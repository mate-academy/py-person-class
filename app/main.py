class Person:
    people = {}

    def __init__(self, name, age):
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    ppl_list = [Person(pers["name"], pers["age"]) for pers in people]

    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
        elif "husband" in pers and pers["husband"] is not None:
            Person.people[pers["name"]].husband = Person.people[pers[
                "husband"]]

    return ppl_list
