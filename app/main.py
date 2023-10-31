class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(pl["name"], pl["age"]) for pl in people]
    for pl in people:
        person = Person.people[pl["name"]]
        if pl.get("wife"):
            person.wife = Person.people[pl["wife"]]
        if pl.get("husband"):
            person.husband = Person.people[pl["husband"]]
    return people_list
