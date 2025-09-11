class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    person_list = []
    for person_dict in people_dicts:
        person_list.append(Person(person_dict["name"], person_dict["age"]))

    for person_dict in people_dicts:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            spouse_name = person_dict["wife"]
            setattr(person_instance, "wife", Person.people[spouse_name])
        elif "husband" in person_dict and person_dict["husband"] is not None:
            spouse_name = person_dict["husband"]
            setattr(person_instance, "husband", Person.people[spouse_name])

    return person_list
