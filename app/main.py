class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"], person_dict["age"]) for person_dict in people]

    for person_dict in people:
        name = person_dict["name"]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            setattr(Person.people[name], "wife", Person.people[wife_name])

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            setattr(Person.people[name], "husband", Person.people[husband_name])

    return person_list
