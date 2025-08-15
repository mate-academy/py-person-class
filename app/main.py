class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def _set_relationship(
    person1: "Person", person2: "Person", relationship_type: str
) -> None:
    if relationship_type == "wife":
        person1.wife = person2
        person2.husband = person1
    elif relationship_type == "husband":
        person1.husband = person2
        person2.wife = person1


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for i, person in enumerate(people):
        if person.get("wife") is not None:
            wife_person = next(
                (p for p in result if p.name == person["wife"]), None
            )
            if wife_person:
                _set_relationship(result[i], wife_person, "wife")

    return result
