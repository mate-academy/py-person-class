class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(man["name"], man["age"]) for man in people]

    for man in people:
        if "wife" in man and man["wife"] is not None:
            Person.people[man["name"]].wife = Person.people[man["wife"]]

        elif "husband" in man and man["husband"] is not None:
            Person.people[man["name"]].husband = Person.people[man["husband"]]

    return person_list
