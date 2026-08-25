
class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(humans: list[dict]) -> list[Person]:
    # Create all Person objects
    result = [Person(person["name"], person["age"]) for person in humans]

    # Connect wife/husband
    for person in humans:
        current_person = Person.people[person["name"]]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]
    return result


people = []

person_list = create_person_list(people)
