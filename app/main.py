class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_instances = []

    for person_dict in people:
        instance = Person(
            name=person_dict["name"], age=person_dict["age"]
        )
        person_instances.append(instance)

    for person_dict in people:
        name = person_dict["name"]
        current_instance = Person.people[name]

        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict[spouse_key]

        if spouse_name is not None:
            spouse_instance = Person.people[spouse_name]
            setattr(current_instance, spouse_key, spouse_instance)

    return person_instances
