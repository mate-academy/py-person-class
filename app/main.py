class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    people_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife
        elif person.get("husband") is not None:
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband
    return people_list
