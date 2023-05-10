class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people: list[dict]) -> list[Person]:
    person_list: list[Person] = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        if person.get("wife") is not None:
            wife_name: str = person.get("wife")
            wife: Person = Person.people.get(wife_name)
            husband_name: str = person.get("name")
            husband: Person = Person.people.get(husband_name)
            husband.wife = wife
            wife.husband = husband
    return person_list
