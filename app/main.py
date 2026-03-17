class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(p["name"], p["age"]) for p in people]
    for src, inst in zip(people, result):
        wife_name = src.get("wife")
        husb_name = src.get("husband")
        if wife_name is not None:
            inst.wife = Person.people[wife_name]
        if husb_name is not None:
            inst.husband = Person.people[husb_name]
    return result
