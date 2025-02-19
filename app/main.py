class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        result.append(person)

    for i, person_dict in enumerate(people):
        if "wife" in person_dict and person_dict["wife"]:
            result[i].wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"]:
            result[i].husband = Person.people[person_dict["husband"]]

    return result
