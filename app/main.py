class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    n_list = [Person(p["name"], p["age"]) for p in people]
    for person_data in people:
        person = Person.people.get(person_data.get("name"))
        if person_data.get("wife"):
            person.wife = Person.people.get(person_data.get("wife"))
        if person_data.get("husband"):
            person.husband = Person.people.get(person_data.get("husband"))
    return n_list
