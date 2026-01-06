class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people.clear()
    persons = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        if data.get("wife"):
            person.wife = Person.people[data["wife"]]

        if data.get("husband"):
            person.husband = Person.people[data["husband"]]

    return persons
