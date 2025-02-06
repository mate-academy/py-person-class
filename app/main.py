class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]
        spouse_key = "wife" if "wife" in person else "husband"

        if (
            spouse_key in person
            and person[spouse_key] is not None
        ):
            setattr(
                person_instance,
                spouse_key,
                Person.people[person[spouse_key]],
            )

    return person_list
