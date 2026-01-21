class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if person_data.get("wife"):
            person.wife = Person.people.get(person_data["wife"])

        if person_data.get("husband"):
            person.husband = Person.people.get(person_data["husband"])

    return person_list
