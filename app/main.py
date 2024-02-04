class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [
        Person(human.get("name"), human.get("age"))
        for human in people
    ]
    for i, person in enumerate(people):
        if person.get("wife"):
            person_list[i].wife = Person.people[person.get("wife")]
        if person.get("husband"):
            person_list[i].husband = Person.people[person.get("husband")]
    return person_list
