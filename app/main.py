class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    persons = [
        Person(
            p.get("name"),
            p.get("age")
        )
        for p in people
    ]

    for person_dict in people:
        name = person_dict["name"]
        current = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name:
            partner = Person.people[wife_name]
            current.wife = partner
            partner.husband = current

        husband_name = person_dict.get("husband")
        if husband_name:
            partner = Person.people[husband_name]
            current.husband = partner
            partner.wife = current

    return persons
