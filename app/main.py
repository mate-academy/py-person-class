class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    people_mapped: list[Person] = []

    for person in people:
        people_mapped.append(create_person(person))

    for person in people:
        if person.get("wife"):
            person_mapped = next((
                p
                for p in people_mapped if
                p.name == person.get("name"))
            )

            set_wife(person_mapped, person.get("wife"))

        if person.get("husband"):
            person_mapped = next((
                p
                for p in people_mapped
                if p.name == person.get("name"))
            )

            set_husband(person_mapped, person.get("husband"))

    return people_mapped


def create_person(person: dict) -> Person:
    return Person(person.get("name"), person.get("age"))


def set_wife(person: Person, wife_name: str) -> None:
    person.wife = Person.people.get(wife_name)


def set_husband(person: Person, husband_name: str) -> None:
    person.husband = Person.people.get(husband_name)
