class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    [Person(person.get("name"), person.get("age")) for person in people]

    for person in people:
        person_instance = Person.people.get(person.get("name"))
        if person.get("wife"):
            person_instance.wife = Person.people.get(person.get("wife"))
        if person.get("husband"):
            person_instance.husband = Person.people.get(person.get("husband"))

    return list(Person.people.values())
