class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
    for person in people:
        if person.get("husband") is not None:
            wife = Person.people[person["name"]]
            husband = Person.people[person["husband"]]
            wife.husband = husband
            husband.wife = wife
    return person_list
