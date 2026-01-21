class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    pass


def create_person_list(people: list[Person]) -> list:
    result = []
    couples = {}

    for persone in people:
        person = Person(name=persone["name"], age=persone["age"])
        result.append(person)
        couples[person.name] = person

    for persone in people:
        if "wife" in persone and persone["wife"]:
            couples[persone["name"]].wife = couples.get(persone["wife"])
        if "husband" in persone and persone["husband"]:
            couples[persone["name"]].husband = couples.get(persone["husband"])

    return result
