class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(info["name"], info["age"]) for info in people]

    for person in people:
        result = Person.people.get(person["name"])
        if person.get("wife") and person["wife"] is not None:
            result.wife = Person.people.get(person["wife"])
        elif person.get("husband") and person["husband"] is not None:
            result.husband = Person.people.get(person["husband"])

    return person_list
