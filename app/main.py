class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    person_list_result = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person in Person.people.values():
        person_data = next(
            data for data in people if data["name"] == person.name
        )

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)

        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list_result
