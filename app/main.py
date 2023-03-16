class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_people = [
        Person(person.get("name"), person.get("age")) for person in people
    ]
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            Person.people[person.get("name")].wife = Person.people[person.get("wife")]

        if "husband" in person and person.get("husband") is not None:
            Person.people[person.get("name")].husband = (
                Person.people[person.get("husband")]
            )
    return list_people
