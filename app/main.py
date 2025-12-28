class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("husband"):
            wife = Person.people[person["name"]]
            husband = Person.people[person["husband"]]
            wife.husband = husband
            husband.wife = wife
    return people_list
