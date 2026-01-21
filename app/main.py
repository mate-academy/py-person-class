class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    res = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        if person.get("wife"):
            Person.people[name].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[name].husband = Person.people[person["husband"]]
    return res
