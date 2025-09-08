class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    result: list[Person] = []
    for data in people:
        person = Person(name=data["name"], age=data["age"])
        result.append(person)

    for data in people:
        current = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            partner = Person.people[data["wife"]]
            current.wife = partner
            partner.husband = current
        if "husband" in data and data["husband"] is not None:
            partner = Person.people[data["husband"]]
            current.husband = partner
            partner.wife = current

    return result
