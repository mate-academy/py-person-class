class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(dict["name"], dict["age"]) for dict in people]
    for dic in people:
        if "wife" in dic and dic["wife"]:
            Person.people[dic["name"]].wife = Person.people[dic["wife"]]
        if "husband" in dic and dic["husband"]:
            Person.people[dic["name"]].husband = Person.people[dic["husband"]]
    return person_list
