class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(item["name"], item["age"]) for item in people]

    for item in people:
        current = Person.people[item["name"]]

        if item.get("wife") and item["wife"] in Person.people:
            current.wife = Person.people[item["wife"]]

        if item.get("husband") and item["husband"] in Person.people:
            current.husband = Person.people[item["husband"]]

    return person_list
