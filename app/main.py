class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if "wife" in person and person["wife"]:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if "husband" in person and person["husband"]:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return persons
