class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]
    for person_dict, person in zip(people, result):
        for attr in ("wife", "husband"):
            if person_dict.get(attr):
                setattr(person, attr, Person.people[person_dict[attr]])
    return result
