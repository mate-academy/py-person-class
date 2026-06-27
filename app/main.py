class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for data in people:
        result.append(Person(data["name"], data["age"]))

    for data, person in zip(people, result):
        if data.get("wife"):
            person.wife = Person.people[data["wife"]]

        if data.get("husband"):
            person.husband = Person.people[data["husband"]]

    return result
