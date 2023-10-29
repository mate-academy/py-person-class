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
        output_list.append(pers_inst)

        if "wife" in pers and pers["wife"] is not None:
            output_list[-1].wife = pers["wife"]
        elif "husband" in pers and pers["husband"] is not None:
            output_list[-1].husband = pers["husband"]
    for i in range(len(output_list)):
        if hasattr(output_list[i], "wife"):
            output_list[i].wife = Person.people[output_list[i].wife]
        if hasattr(output_list[i], "husband"):
            output_list[i].husband = Person.people[output_list[i].husband]

    return output_list
