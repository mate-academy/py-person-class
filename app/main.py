class Person:
    """Representa uma pessoa com nome, idade e possíveis relacionamentos."""

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict[str, object]]) -> list[Person]:
    """Cria uma lista de instâncias Person a partir de uma lista de dicionários."""
    persons = [
        Person(str(p["name"]), int(p["age"]))
        for p in people_data
    ]

    for data in people_data:
        person = Person.people[data["name"]]
        wife_name = data.get("wife")
        husband_name = data.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return persons
