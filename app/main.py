class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for member in people:
        member_name = Person.people[member["name"]]
        if member.get("wife"):
            member_name.wife = Person.people[member["wife"]]
        if member.get("husband"):
            member_name.husband = Person.people[member["husband"]]

    return person_list
