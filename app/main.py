class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people1: list) -> list:
    output_list = []
    for pers in people1:
        pers_inst = Person(pers["name"], pers["age"])
        if "wife" in pers and pers["wife"] is not None:
            pers_inst.wife = pers["wife"]
        elif "husband" in pers and pers["husband"] is not None:
            pers_inst.husband = pers["husband"]
    for pers1 in Person.people:
        if hasattr(Person.people[pers1], "wife"):
            Person.people[pers1].wife =\
                Person.people[Person.people[pers1].wife]
        if hasattr(Person.people[pers1], "husband"):
            Person.people[pers1].husband =\
                Person.people[Person.people[pers1].husband]
        output_list.append(Person.people[pers1])
    return output_list
