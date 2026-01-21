class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    for data in people:
        Person(data["name"], data["age"])

    for data in people:
        person = Person.people[data["name"]]

        if data.get("wife"):
            person.wife = Person.people[data["wife"]]
        if data.get("husband"):
            person.husband = Person.people[data["husband"]]

    return [Person.people[data["name"]] for data in people]
