class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    instances = [Person(name=d["name"], age=d["age"]) for d in people]

    for d in people:
        current = Person.people[d["name"]]
        wife_name = d.get("wife")
        if wife_name:
            current.wife = Person.people[wife_name]
        husband_name = d.get("husband")
        if husband_name:
            current.husband = Person.people[husband_name]

    return instances
