class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people: list) -> list:
    person_list = []

    # Create all people
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    # Set up a wife/husband connection
    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return person_list
