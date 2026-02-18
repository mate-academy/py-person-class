class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    result: list[Person] = []

    for person_dict in people:
        result.append(Person(person_dict["name"], person_dict["age"]))

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person_obj.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            person_obj.husband = Person.people[person_dict["husband"]]

    return result
