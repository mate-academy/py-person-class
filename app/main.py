class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_objects = []

    for person_info in people:

        person = Person(
            person_info.get("name"),
            person_info.get("age")
        )
        person_objects.append(person)

    for person_info in people:

        person_name = person_info.get("name")
        person = Person.people.get(person_name)

        wife_name = person_info.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = person_info.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_objects
