class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person_data in people:
        per = Person(person_data["name"], person_data["age"])
        persons.append(per)

    for person_data in people:
        current = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            current.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"]:
            current.husband = Person.people[person_data["husband"]]

    return persons
