class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]
            husband.wife = wife
            wife.husband = husband

        if person.get("husband"):
            husband = Person.people[person["husband"]]
            wife = Person.people[person["name"]]
            wife.husband = husband
            husband.wife = wife

    return result
