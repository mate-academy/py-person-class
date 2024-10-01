class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data.get("name"), person_data.get("age"))
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data.get("name")]
        if "wife" in person_data and person_data.get("wife") is not None:
            person.wife = Person.people[person_data.get("wife")]
        if "husband" in person_data and person_data.get("husband") is not None:
            person.husband = Person.people[person_data.get("husband")]

    return person_list
