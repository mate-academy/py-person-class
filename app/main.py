class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for item in people:
        Person(item["name"], item["age"])

    for item in people:
        if "wife" in item and item["wife"] is not None:
            person = Person.people[item["name"]]
            person.wife = Person.people[item["wife"]]

        if "husband" in item and item["husband"] is not None:
            person = Person.people[item["name"]]
            person.husband = Person.people[item["husband"]]

    return list(Person.people.values())
