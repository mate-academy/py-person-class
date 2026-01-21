class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for index, man in enumerate(people):
        if man.get("wife"):
            persons_list[index].wife = Person.people[man.get("wife")]
        elif man.get("husband"):
            persons_list[index].husband = Person.people[man.get("husband")]
    return persons_list
