class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list["Person"]:  # type: ignore
    persons = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]
    for person_dict in people:

        person = Person.people[person_dict["name"]]
        spouse_key = (
            "wife"
            if "wife" in person_dict
            else "husband" if "husband" in person_dict else None
        )
        if spouse_key and person_dict[spouse_key]:
            spouse_name = person_dict[spouse_key]
            setattr(person, spouse_key, Person.people[spouse_name])

    return persons
