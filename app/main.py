class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(info["name"], info["age"]) for info in people]

    for info in people:
        person = Person.people[info["name"]]

        if info.get("wife"):
            person.wife = Person.people[info["wife"]]

        if info.get("husband"):
            person.husband = Person.people[info["husband"]]

    return result
