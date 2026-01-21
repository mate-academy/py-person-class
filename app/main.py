class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    persons = [Person(data["name"], data["age"]) for data in people]
    for data in people:
        obj = Person.people[data["name"]]
        wife_name = data.get("wife")
        if wife_name:
            obj.wife = Person.people[wife_name]
        husband_name = data.get("husband")
        if husband_name:
            obj.husband = Person.people[husband_name]
    return persons
