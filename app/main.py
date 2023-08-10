class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for man in people:
        person = Person(man["name"], man["age"])
        person_list.append(person)

    for man in people:
        if "wife" in man and man["wife"] is not None:
            husband = Person.people[man["name"]]
            wife = Person.people[man["wife"]]
            husband.wife = wife
            wife.husband = husband

    return person_list
