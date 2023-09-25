class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    res_list: list = [Person(pers["name"], pers["age"]) for pers in people]
    for elem in people:
        if elem.get("wife"):
            Person.people[elem.get("wife")].husband = Person.people[elem["name"]]
            Person.people[elem["name"]].wife = Person.people[elem.get("wife")]
    return res_list
