class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    [
        Person(person.get("name"), person.get("age"))
        for person in people
        if person.get("name") not in Person.people
    ]

    for person in people:
        person_instance = Person.people.get(person.get("name"))
        if person.get("husband") is not None:
            person_instance.husband = Person.people.get(person.get("husband"))
        if person.get("wife") is not None:
            person_instance.wife = Person.people.get(person.get("wife"))

    return [Person.people.get(person.get("name")) for person in people]
