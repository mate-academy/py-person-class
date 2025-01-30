class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instance_list = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        pair = Person.people.get(person["name"])
        if person.get("wife"):
            pair.wife = Person.people.get(person["wife"])
        elif person.get("husband"):
            pair.husband = Person.people.get(person["husband"])

    return instance_list
