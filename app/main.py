

class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = dict()
    persons = [Person(man["name"], man["age"]) for man in people]
    for man in people:
        person = Person.people[man["name"]]
        if man.get("wife") is not None:
            person.wife = Person.people[man["wife"]]
        if man.get("husband") is not None:
            person.husband = Person.people[man["husband"]]
    return persons
