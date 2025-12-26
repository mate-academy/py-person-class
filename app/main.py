class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Person | None = None
        self.husband: Person | None = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name=\"{self.name}\", age={self.age})"


def create_person_list(people_data: list[dict[str, str | int]]) -> list[Person]:
    Person.people = {}

    people = [Person(p["name"], p["age"]) for p in people_data]

    for data in people_data:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name:
            wife = Person.people.get(wife_name)
            if wife and person.wife is None:
                person.wife = wife
                if wife.husband is None:
                    wife.husband = person

        husband_name = data.get("husband")
        if husband_name:
            husband = Person.people.get(husband_name)
            if husband and person.husband is None:
                person.husband = husband
                if husband.wife is None:
                    husband.wife = person

    return people

