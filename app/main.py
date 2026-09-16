class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for item in people:
        Person(item["name"], item["age"])

    for item in people:
        new_person = Person.people[item["name"]]

        if item.get("wife"):
            new_person.wife = Person.people[item["wife"]]

        if item.get("husband"):
            new_person.husband = Person.people[item["husband"]]

    return [Person.people[item["name"]] for item in people]
