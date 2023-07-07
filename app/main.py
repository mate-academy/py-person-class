class Person:

    people = {Person.name: Person}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def create_person_list(people: list) -> list:
        for individual in people:
            Person(
                name=individual["name"],
                age=individual["age"],
            )
            if "wife" in individual:
                Person["wife"] =
