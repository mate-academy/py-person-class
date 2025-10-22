class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people_data: list[dict[str, object]]
) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"]) for person in people_data
    ]
    for person_info in people_data:
        current_person = Person.people[person_info["name"]]
        if "wife" in person_info and person_info["wife"] is not None:
            current_person.wife = Person.people[person_info["wife"]]
        if "husband" in person_info and person_info["husband"] is not None:
            current_person.husband = Person.people[person_info["husband"]]
    return person_list
