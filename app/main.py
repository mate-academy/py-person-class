class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person((man["name"]), man["age"]) for man in people]
    for guy in people:
        if guy.get("wife"):
            Person.people[guy["name"]].wife = Person.people[guy["wife"]]
        elif guy.get("husband"):
            Person.people[guy["name"]].husband = Person.people[guy["husband"]]
    return person_list
