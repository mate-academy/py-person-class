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

    for index, value in enumerate(result):

        wife_name = people[index].get("wife")
        husband_name = people[index].get("husband")

        if wife_name:
            result[index].wife = Person.people[
                people[index]["wife"]
            ]

        if husband_name:
            result[index].husband = Person.people[
                people[index]["husband"]
            ]

    return result
