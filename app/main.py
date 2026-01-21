class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    peoples = [Person(man["name"], man["age"]) for man in people]

    for man in people:
        if man.get("wife"):
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        if man.get("husband"):
            Person.people[man["name"]].husband = Person.people[man["husband"]]

    return peoples
