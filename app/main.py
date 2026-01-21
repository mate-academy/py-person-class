class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name.lower()] = self


def create_person_list(people_data: list) -> list:
    name_to_person = {person_data["name"]: Person(
        name=person_data["name"], age=person_data["age"]
    ) for person_data in people_data}

    for person_data in people_data:
        person = name_to_person[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = name_to_person[person_data["wife"]]
        if "husband" in person_data and person_data["husband"]:
            person.husband = name_to_person[person_data["husband"]]

    return list(name_to_person.values())
