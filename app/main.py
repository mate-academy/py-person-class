class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person_info in people:
        Person(person_info["name"], person_info["age"])
    for person_info in people:
        person = Person.people[person_info["name"]]
        if "wife" in person_info and person_info["wife"] is not None:
            wife = Person.people[person_info["wife"]]
            if wife is None:
                continue
            setattr(person, "wife", wife)
            setattr(wife, "husband", person)
    return list(Person.people.values())
