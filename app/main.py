class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(per["name"], per["age"]) for per in people]
    for person in people:
        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return persons_list
