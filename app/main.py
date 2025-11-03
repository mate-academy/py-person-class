class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [
        Person(
            person_data.get("name"),
            person_data.get("age")
        )
        for person_data in people
    ]

    for person_data in people:
        person = Person.people.get(person_data.get("name"))

        wife_name = person_data.get("wife")
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]
    return result
