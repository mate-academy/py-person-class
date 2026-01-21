class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list[dict[str, any]]) -> list[Person]:
    new_person_list = [
        Person(person.get("name"), person.get("age")) for person in people_list
    ]

    for person in people_list:
        if person.get("wife") and person["wife"] in Person.people:
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife

        if person.get("husband") and person["husband"] in Person.people:
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband

    return new_person_list
