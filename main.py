class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Reset globalnego rejestru osób
    Person.people.clear()

    # Faza 1: Tworzenie instancji
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Faza 2: Ustawianie relacji małżeńskich
    for person in people:
        current = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            spouse = Person.people.get(person["wife"])
            if spouse:
                current.wife = spouse

        elif "husband" in person and person["husband"] is not None:
            spouse = Person.people.get(person["husband"])
            if spouse:
                current.husband = spouse

    return person_list
