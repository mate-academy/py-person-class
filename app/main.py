class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people.get(person_data["wife"])

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people.get(person_data["husband"])

    return person_list
