class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list: list[Person] = []

    for person_dict in people:
        person_list.append(Person(person_dict["name"], person_dict["age"]))

    for person_dict in people:
        name = person_dict["name"]

        if "wife" in person_dict and person_dict["wife"] is not None:
            setattr(Person.people[name], "wife", Person.people[person_dict["wife"]])

        if "husband" in person_dict and person_dict["husband"] is not None:
            setattr(
                Person.people[name], "husband", Person.people[person_dict["husband"]]
            )

    return person_list
