class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict, person in zip(people, person_list):
        for key in ("wife", "husband"):
            spouse_name = person_dict.get(key)
            if spouse_name is not None:
                setattr(person, key, Person.people[spouse_name])

    return person_list
