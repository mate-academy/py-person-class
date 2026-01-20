class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        name = person["name"]
        age = person["age"]
        Person.person(name, age)

    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            current_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            current_person.husband = Person.people[person["husband"]]
    return list(Person.people.values())
