class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = []
    for person in people:
        new_people.append(Person(person.get("name"), person.get("age")))
    for i, person in enumerate(people):
        if "wife" in person and person.get("wife") is not None:
            new_people[i].wife = Person.people.get(person["wife"])
        if "husband" in person and person.get("husband") is not None:
            new_people[i].husband = Person.people.get(person["husband"])
    return new_people
