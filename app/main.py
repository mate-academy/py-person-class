class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for married in people:
        name = married.get("name")
        current_person = Person.people[name]

        wife_name = married.get("wife")
        if wife_name is not None:
            current_person.wife = Person.people[wife_name]

        husband_name = married.get("husband")
        if husband_name is not None:
            current_person.husband = Person.people[husband_name]

    return person_list
