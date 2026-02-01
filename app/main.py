class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(data: list[dict]) -> list[Person]:
    persons = [Person(item["name"], item["age"]) for item in data]

    for item in data:
        person = Person.people[item["name"]]

        if item.get("wife"):
            person.wife = Person.people[item["wife"]]

        if item.get("husband"):
            person.husband = Person.people[item["husband"]]

    return persons
