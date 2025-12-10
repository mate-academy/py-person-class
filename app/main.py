class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        def create_person_list(people: list[dict[str, object]]) -> list[Person]:
    person_list = [Person(p["name"], p["age"]) for p in people]
    for p in people:
        person_instance = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            person_instance.wife = Person.people[p["wife"]]
        if "husband" in p and p["husband"] is not None:
            person_instance.husband = Person.people[p["husband"]]

    return person_list
