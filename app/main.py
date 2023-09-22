class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    res_list: list = [Person(pers["name"], pers["age"]) for pers in people]
    for elem in people:
        if "wife" in elem.keys() and elem["wife"] is not None:
            for key in Person.people:
                if key == elem["wife"]:
                    Person.people[elem["name"]].wife = Person.people[key]
                    Person.people[key].husband = Person.people[elem["name"]]
                    break
    return res_list
