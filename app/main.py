class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(man["name"], man["age"]) for man in people]

    for man in people:
        if "wife" in man and man.get("wife") is not None:
            Person.people[man["name"]].wife = Person.people[man["wife"]]

        if "husband" in man and man.get("husband") is not None:
            Person.people[man["name"]].husband = Person.people[man["husband"]]

    return person_list
