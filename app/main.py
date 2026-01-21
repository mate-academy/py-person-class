class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_raw in people:
        person = Person(person_raw["name"], person_raw["age"])
        result.append(person)

    for person_raw in people:
        if "husband" in person_raw.keys() and person_raw["husband"]:
            Person.people[person_raw["name"]].husband \
                = Person.people[person_raw["husband"]]
        if "wife" in person_raw.keys() and person_raw["wife"]:
            Person.people[person_raw["name"]].wife \
                = Person.people[person_raw["wife"]]

    return result
