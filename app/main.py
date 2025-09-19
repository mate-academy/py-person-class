class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    humans = []
    for human in people:
        person = Person(human["name"], human["age"])
        humans.append(person)

    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"] is not None:
            person.wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            person.husband = Person.people[human["husband"]]

    return humans

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
