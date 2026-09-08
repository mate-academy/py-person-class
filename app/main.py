class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]

    for person_dict in people:
        name = person_dict["name"]
        current_instance = Person.people[name]

        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        spouse_key = "wife" if person_dict.get("wife") else "husband"

        if spouse_name is not None:
            spouse_instance = Person.people[spouse_name]
            setattr(current_instance, spouse_key, spouse_instance)

    return person_instances
