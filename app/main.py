class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(
            person_data["name"],
            person_data["age"]
        )

        person_list.append(person)

    for person_data in people:
        current_person = Person.people[
            person_data["name"]
        ]
        if ("wife" in person_data and person_data["wife"] is not None):
            wife_name = person_data["wife"]

            current_person.wife = (Person.people[wife_name])
        if ("husband" in person_data and person_data["husband"] is not None):
            husband_name = person_data["husband"]

            current_person.husband = (Person.people[husband_name])
    return person_list
