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
        current_person = Person.people[item["name"]]

        if item.get("wife"):
            current_person.wife = Person.people[item["wife"]]

        if item.get("husband"):
            current_person.husband = Person.people[item["husband"]]

    return list(Person.people.values())
