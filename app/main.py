class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data: list[dict]) -> list[Person]:
    persons = []

    for person_data in data:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        persons.append(person)

    for person_data in data:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return persons
