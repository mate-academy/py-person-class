class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    Person.people = {}

    person_instances: list[Person] = [
        Person(person_dict["name"], person_dict["age"]) for person_dict in people
    ]

    for person_dict in people:
        person = Person.people.get(person_dict["name"])

        spouse_name = person_dict.get("wife")
        spouse_key = "wife"

        if spouse_name is None:
            spouse_name = person_dict.get("husband")
            spouse_key = "husband"

        if spouse_name is None:
            continue

        spouse = Person.people.get(spouse_name)
        if spouse is None:
            continue

        setattr(person, spouse_key, spouse)

    return person_instances
