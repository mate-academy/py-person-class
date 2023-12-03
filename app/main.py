class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for pers in people:
        human = Person(pers["name"], pers["age"])
        result.append(human)

    for i in range(len(result)):

        wife_name = people[i].get("wife")
        husband_name = people[i].get("husband")

        if wife_name:
            result[i].wife = Person.people[
                people[i]["wife"]
            ]

        if husband_name:
            result[i].husband = Person.people[
                people[i]["husband"]
            ]

    return result
