class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_list = [Person(man["name"], man["age"]) for man in people]
    for man in people:
        person = Person.people[man["name"]]
        if man.get("wife"):
            person.wife = Person.people[man["wife"]]
        if man.get("husband"):
            person.husband = Person.people[man["husband"]]
    return people_list
