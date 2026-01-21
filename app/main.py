class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        current = Person.people[name]
        if "wife" in person and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            current.wife = wife
            wife.husband = current
        if "husband" in person and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            current.husband = husband
            husband.wife = current
    return person_list
