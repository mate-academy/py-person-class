class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for member in people:
        result.append(Person(member["name"], member["age"]))

    for member in people:
        person = Person.people[member["name"]]

        if member.get("wife") is not None:
            person.wife = Person.people[member["wife"]]

        if member.get("husband") is not None:
            person.husband = Person.people[member["husband"]]

    return result
