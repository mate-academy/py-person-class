class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_map = {}
    for person in people:
        name = person["name"]
        age = person["age"]
        person_map[name] = Person(name, age)

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"] is not None:
            person_map[name].wife = person_map[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person_map[name].husband = person_map[person["husband"]]

    return list(person_map.values())
