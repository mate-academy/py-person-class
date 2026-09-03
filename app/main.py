class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    person_instances = [Person(p["name"], p["age"]) for p in people]

    for p_dict in people:
        for key in ("wife", "husband"):
            spouse_name = p_dict.get(key)
            if spouse_name is not None:
                spouse_instance = Person.people[spouse_name]
                current_person = Person.people[p_dict["name"]]
                setattr(current_person, key, spouse_instance)

    return person_instances
