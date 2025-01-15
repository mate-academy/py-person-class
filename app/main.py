class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        if person.get("wife") is not None:
            result[i].wife = Person.people.get(person["wife"])
        if person.get("husband") is not None:
            result[i].husband = Person.people.get(person["husband"])

    return result
