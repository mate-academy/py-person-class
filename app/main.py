class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people_data
    ]

    for person_data in people_data:
        current_person = Person.people.get(person_data.get("name"))

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            current_person.wife = Person.people.get(wife_name)

        if husband_name:
            current_person.husband = Person.people.get(husband_name)

    return person_list
