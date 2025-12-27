class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: "Person" | None = None
        self.husband: "Person" | None = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list[dict[str, object]]) -> list[Person]:
    person_list: list[Person] = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person_instance: Person = Person.people[p["name"]]
        wife_name = p.get("wife")
        husband_name = p.get("husband")
        person_instance.wife = (
            Person.people.get(wife_name) if wife_name else None
        )
        person_instance.husband = (
            Person.people.get(husband_name) if husband_name else None
        )

    return person_list


# Exemplo de uso
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]

person_list = create_person_list(people)
print(person_list)  # Lista de instâncias de Person
print(Person.people)  # Dicionário com referências às instâncias
