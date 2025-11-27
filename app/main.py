class Person:
    person = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.person[self.name] = self


def create_person_list(people: list) -> list:
    for p in people:
        Person(p["name"], p["age"])
    for p in people:
        person_instance = Person.person[p["name"]]

        if p.get("husband"):
            person_instance.husband = Person.person[p["husband"]]

        if p.get("wife"):
            person_instance.wife = Person.person[p["wife"]]

    return list(Person.person.values())
