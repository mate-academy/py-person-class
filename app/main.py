class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data: list[dict]) -> list:
    person_list = []
    for entry in data:
        person = Person(entry["name"], entry["age"])
        person_list.append(person)

    for entry in data:
        person = Person.people[entry["name"]]
        if "wife" in entry and entry["wife"]:
            setattr(person, "wife", Person.people[entry["wife"]])
        if "husband" in entry and entry["husband"]:
            setattr(person, "husband", Person.people[entry["husband"]])
    return person_list
