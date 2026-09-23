class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    people_data = [
        Person(person_data.get("name"), person_data.get("age"))
        for person_data in people
    ]

    all_people = Person.people
    for person_data in people:
        if person_data.get("wife") is not None:
            all_people[
                person_data.get("name")
            ].wife = (
                all_people)[
                person_data.get("wife")
            ]

        if person_data.get("husband") is not None:
            all_people[
                person_data.get("name")
            ].husband = (
                all_people)[
                person_data.get("husband")
            ]

    return people_data
