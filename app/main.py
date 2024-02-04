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
    for i, person in enumerate(people):
        if person.get("wife"):
            people_instances[i].wife = Person.people[person.get("wife")]
        if person.get("husband"):
            people_instances[i].husband = Person.people[person.get("husband")]
    return people_instances
