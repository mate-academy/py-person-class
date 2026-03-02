class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    person_list = [Person(p["name"], p["age"]) for p in people]

    for person_data in people:
        person_instance = Person.people[person_data["name"]]

        if person_data.get("wife"):
            person_instance.wife = Person.people[person_data["wife"]]

        if person_data.get("husband"):
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list
