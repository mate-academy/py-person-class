class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        Person(
            name=person_data["name"],
            age=person_data["age"]
        )

    for person_data in people:
        name = person_data["name"]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            Person.people[name].wife = Person.people[wife_name]
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            Person.people[name].husband = Person.people[husband_name]

    return list(Person.people.values())
