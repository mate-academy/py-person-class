class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data: list[dict]) -> list[Person]:
    Person.people.clear()

    for item in data:
        Person(name=item["name"], age=item["age"])

    for item in data:
        person = Person.people[item["name"]]
        if "wife" in item and item["wife"] is not None:
            person.wife = Person.people[item["wife"]]
        if "husband" in item and item["husband"] is not None:
            person.husband = Person.people[item["husband"]]

    return [Person.people[item["name"]] for item in data]
