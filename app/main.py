class Person:
    people: dict[str, "Person"] = {}

    def __init__(self: "Person", name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    instances = [Person(name=p["name"], age=p["age"]) for p in people]

    for person_dict, person_instance in zip(people, instances):
        if "wife" in person_dict and person_dict.get("wife") is not None:
            person_instance.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict.get("husband") is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

    return instances
