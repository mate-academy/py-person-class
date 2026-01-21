class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(person.get("name"), person.get("age")) for person in people]
    for person in people:
        person_list = Person.people.get(person["name"])
        if person.get("wife"):
            person_list.wife = Person.people.get(person["wife"])
        if person.get("husband"):
            person_list.husband = Person.people.get(person["husband"])

    return person_instances
