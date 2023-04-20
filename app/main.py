class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "husband" in person and person["husband"] is not None:
            wife = Person.people[person["name"]]
            husband = Person.people[person["husband"]]
            wife.husband = husband
            husband.wife = wife
    return result
