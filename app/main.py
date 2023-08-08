class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        Person(person.get("name"), person.get("age"))

    for person in people:
        if person.get("wife"):
            person_obj = Person.people.get(person.get("name"))
            person_obj.wife = Person.people.get(person.get("wife"))
        elif person.get("husband"):
            person_obj = Person.people.get(person.get("name"))
            person_obj.husband = Person.people.get(person.get("husband"))

    return list(Person.people.values())
