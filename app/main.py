class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    person_instances = [
        Person(name=p.get("name"), age=p.get("age")) for p in people
    ]

    for person_dict in people:
        name = person_dict.get("name")
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)

        if spouse_name is not None:
            current_person = Person.people.get(name)
            spouse_object = Person.people.get(spouse_name)

            setattr(current_person, spouse_key, spouse_object)

            inverse_key = "husband" if spouse_key == "wife" else "wife"
            setattr(spouse_object, inverse_key, current_person)

    return person_instances
