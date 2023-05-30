class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(
            person_data["name"],
            person_data["age"]
        )
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]
        wife_name = person_data["wife"] if "wife" in person_data else None
        if wife_name:
            person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person

    return person_list
