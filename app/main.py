class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    result = [
        Person(person.get("name"), person.get("age"))
        for person in people
        if person.get("name") is not None and person.get("age") is not None
    ]

    for person_dict in people:
        name = person_dict.get("name")
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        current_person = Person.people.get(name)
        if current_person is None:
            continue

        if wife_name:
            current_person.wife = Person.people.get(wife_name)
        if husband_name:
            current_person.husband = Person.people.get(husband_name)

    return result
