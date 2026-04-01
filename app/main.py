class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people.clear()

    instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_instance = Person.people[person_data["name"]]

        if person_data.get("wife"):
            current_instance.wife = Person.people[person_data.get("wife")]

        if person_data.get("husband"):
            current_instance.husband = Person.people[person_data.get("husband")]

    return instances
