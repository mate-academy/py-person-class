class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = []

    for entry in people:
        person = Person(entry["name"], entry["age"])
        person_list.append(person)

    for entry in people:
        person = Person.people[entry["name"]]

        if entry.get("wife") is not None:
            person.wife = Person.people[entry["wife"]]

        if entry.get("husband") is not None:
            person.husband = Person.people[entry["husband"]]

    return person_list
