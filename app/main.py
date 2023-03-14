class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(
        people_dicts: list[dict[str, str | int | None]]
) -> list:
    people_instances = [
        Person(person_dict.get("name"), person_dict.get("age"))
        for person_dict in people_dicts
    ]

    for person_dict, person_instance in zip(people_dicts, people_instances):
        if "wife" in person_dict and person_dict.get("wife") is not None:
            person_instance.wife = Person.people.get(person_dict.get("wife"))

        if "husband" in person_dict and person_dict.get("husband") is not None:
            person_instance.husband = \
                Person.people.get(person_dict.get("husband"))

    return people_instances
