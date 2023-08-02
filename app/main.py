class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        new_person = Person(person.get("name"), person.get("age"))
        person_list.append(new_person)

    for member in people:
        member_code = Person.people[member["name"]]
        if member.get("wife"):
            member_code.wife = Person.people[member["wife"]]
        if member.get("husband"):
            member_code.husband = Person.people[member["husband"]]

    return person_list
