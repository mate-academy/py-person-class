class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(name=person["name"], age=person["age"])
                   for person in people]
    for person in people:
        if person.get("husband") is not None or person.get("wife") is not None:
            wife = Person.people[person["name"]]
            husband = Person.people[person["name"]]
            wife.husband = husband
            husband.wife = wife

    return person_list
