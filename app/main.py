class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    les = []

    for obj in people:
        les.append(Person(obj["name"], obj["age"]))

    for obj in people:
        if "husband" in obj:
            if isinstance(obj["husband"], str):
                Person.people[obj["name"]].husband\
                    = Person.people[obj["husband"]]

    for obj in people:
        if "wife" in obj:
            if isinstance(obj["wife"], str):
                Person.people[obj["name"]].wife = Person.people[obj["wife"]]

    return les
