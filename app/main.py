class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    people_instances = [
        Person(human.get("name"), human.get("age"))
        for human in people
    ]
    for person in people:
        person_instances = Person.people.get(person.get("name"))
        if person.get("wife"):
            person_instances.wife = Person.people.get(person.get("wife"))
        if person.get("husband"):
            person_instances.husband = Person.people.get(person.get("husband"))
    return people_instances
