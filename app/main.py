class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            wife = Person.people[person.get("wife")]
            husband = Person.people[person.get("name")]
            husband.wife = wife
            wife.husband = husband
    return list(Person.people.values())
