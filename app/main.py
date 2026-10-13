class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p.get("name"), p.get("age")) for p in people]

    for p in people:
        person_instance = Person.people[p.get("name")]

        if p.get("wife"):
            person_instance.wife = Person.people[p.get("wife")]

        if p.get("husband"):
            person_instance.husband = Person.people[p.get("husband")]

    return person_list
