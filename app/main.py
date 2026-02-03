class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = []
    for p in people:
        person = Person(p["name"], p["age"])
        person_list.append(person)

    for p in people:
        person = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            person.wife = Person.people[p["wife"]]
        elif "husband" in p and p["husband"] is not None:
            person.husband = Person.people[p["husband"]]

    return person_list
