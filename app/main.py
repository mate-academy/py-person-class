class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    created_list = [Person(person.get("name"),
                           person.get("age"))
                    for person in people]

    for person in people:
        name = person.get("name")
        if person.get("husband"):
            Person.people[name].husband = Person.people[person.get("husband")]

        elif person.get("wife"):
            Person.people[name].wife = Person.people[person.get("wife")]

    return created_list
