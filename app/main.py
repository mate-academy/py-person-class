class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person(person_to_create: dict) -> Person:
    if person_to_create["name"] not in Person.people:
        return Person(person_to_create["name"], person_to_create["age"])

    return Person.people[person_to_create["name"]]


def get_spouse(spouse_name: str, people: list) -> dict:
    return [person for person in people if person["name"] == spouse_name][0]


def create_person_list(people: list) -> list[Person]:
    person_list = []

    for person in people:
        *_, spouse_key = person
        new_person = create_person(person)

        if person.get(spouse_key):
            spouse = get_spouse(person[spouse_key], people)
            setattr(new_person, spouse_key, create_person(spouse))

        person_list.append(new_person)

    return person_list
