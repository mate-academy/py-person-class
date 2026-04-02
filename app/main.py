class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(data: list) -> list:
    Person.people.clear()
    persona = [
        Person(person_data["name"], person_data["age"])
        for person_data in data
    ]

    for person_data in data:
        persona = Person.people[person_data["name"]]

        if person_data.get("wife") is not None:
            persona.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            persona.husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
