class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people = [
        Person(name=data["name"], age=data["age"])
        for data in people
    ]

    for data in people:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]
    return new_people
