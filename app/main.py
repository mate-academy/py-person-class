class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(raw_people: list[dict]) -> list[Person]:
    Person.people.clear()

    created_people = [
        Person(person_data.get("name"), person_data.get("age"))
        for person_data in raw_people
    ]

    for person_data in raw_people:
        person = Person.people[person_data.get("name")]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return created_people
