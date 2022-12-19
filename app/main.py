class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list[dict]) -> list[Person]:

    create_instance = [Person(p["name"], p["age"]) for p in persons]

    for i in range(len(create_instance)):
        if "wife" in persons[i] and persons[i]["wife"] is not None:
            create_instance[i].wife = Person.people[persons[i]["wife"]]

        elif "husband" in persons[i] and persons[i]["husband"] is not None:
            create_instance[i].husband = Person.people[persons[i]["husband"]]

    return create_instance
