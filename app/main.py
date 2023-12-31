class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(man["name"], man["age"]) for man in people]
    for person in people:
        if man.get("wife"):
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        elif man.get("husband"):
            Person.people[man["name"]].husband = Person.people[man["husband"]]
    return person_list
