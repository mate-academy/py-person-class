class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for char in people:
        Person(char["name"], char["age"])

    for char in people:
        person = Person.people[char["name"]]
        if char.get("wife"):
            setattr(person, "wife", Person.people.get(char["wife"]))
        elif char.get("husband"):
            setattr(person, "husband", Person.people.get(char["husband"]))

    return list(Person.people.values())
