class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = []

    for person_dict in people:
        new_person = Person(person_dict["name"], person_dict["age"])
        result.append(new_person)

    for person_dict, person_instance in zip(people, result):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[
                person_dict["wife"]
            ]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[
                person_dict["husband"]
            ]

    return result
