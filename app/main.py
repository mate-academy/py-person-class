class Person:
    people: {str, "Person"} = {}

    def __init__(self, name: str = None, age: int = None) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person.get("name"),
                          person.get("age")) for person in people]
    for person in people:
        if person.get("wife"):
            Person.people.get(person.get("name")).wife = Person.people.get(
                person.get("wife"))
        if person.get("husband"):
            Person.people.get(person.get("name")).husband = Person.people.get(
                person.get("husband"))
    return person_list
