class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(p.get("name"), p.get("age")) for p in people]

    for person_data in people:
        inst = Person.people[person_data["name"]]

        if person_data.get("wife") and person_data["wife"] is not None:
            inst.wife = Person.people[person_data["wife"]]
        if person_data.get("husband") and person_data["husband"] is not None:
            inst.husband = Person.people[person_data["husband"]]

    return result
