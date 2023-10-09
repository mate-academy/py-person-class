class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons_list = [Person(one["name"], one["age"]) for one in people]
    for key, value in enumerate(people):
        if value.get("wife"):
            persons_list[key].wife = Person.people[value.get("wife")]
        elif value.get("husband"):
            persons_list[key].husband = Person.people[value.get("husband")]
    return persons_list
