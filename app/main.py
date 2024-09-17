class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    name_to_person = {
        person_data["name"]: Person(person_data["name"],
        person_data["age"]) for person_data in people
    }
    person_list = list(name_to_person.values())

    for person_data in people:
        person = name_to_person[person_data["name"]]
        if person_data.get("wife") is not None:
            person.wife = name_to_person.get(person_data["wife"])

        if person_data.get("husband") is not None:
            person.husband = name_to_person.get(person_data["husband"])

    return person_list
