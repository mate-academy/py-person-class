class Person:
    people = {}

    def __init__(self, name: str, age: int, spouse=None) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self
        if spouse:
            self.spouse = Person.people.get(spouse)


def create_person_list(people: list) -> list:
    person_list = []
    for p in people:
        person = Person(p["name"], p["age"], p.get["wife"] or p.get("husband"))
        person_list.append(person)
    return person_list
