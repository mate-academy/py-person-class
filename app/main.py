class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(man.get("name"), man.get("age")) for man in people]

    for index, man in enumerate(people):
        if man.get("wife"):
            persons[index].wife = Person.people[man.get("wife")]
        elif man.get("husband"):
            persons[index].husband = Person.people[man.get("husband")]

    return persons
