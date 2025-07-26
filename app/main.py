

class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    persons = []
    for data in people_data:
        person = Person(data["name"], data["age"])
        persons.append(person)

    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]

    return persons
