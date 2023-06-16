class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = []
    for member in people:
        result.append(Person(member["name"], member["age"]))

    for member in people:
        if member.get("wife"):
            Person.people[member["name"]].wife = Person.people[member["wife"]]
        elif member.get("husband"):
            Person.people[member["name"]].husband \
                = Person.people[member["husband"]]

    return result
