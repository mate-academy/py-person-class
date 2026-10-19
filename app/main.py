class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list | None:
    Person.people.clear()
    for person in people:
        name = person.get("name")
        age = person.get("age")
        if name is not None and age is not None:
            Person(name, age)

    for person in people:
        name = person.get("name")
        if name is None or name not in Person.people:
            continue
        current_person = Person.people[name]
        wife_name = person.get("wife")
        if wife_name is not None and wife_name in Person.people:
            current_person.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if husband_name is not None and husband_name in Person.people:
            current_person.husband = Person.people[husband_name]
    result = []
    for person in people:
        name = person.get("name")
        if name in Person.people:
            result.append(Person.people[name])

    return result
