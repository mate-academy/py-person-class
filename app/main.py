class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        result.append(person)

    for i, person_data in enumerate(people):
        if "wife" in person_data and person_data["wife"]:
            result[i].wife = Person.people[person_data["wife"]]
    for i, person_data in enumerate(people):
        if "husband" in person_data and person_data["husband"]:
            result[i].husband = Person.people[person_data["husband"]]
    return result
