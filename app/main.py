class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(data["name"], data["age"])
        for data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if person_data.get("wife") is not None:
            person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            person.husband = Person.people[person_data["husband"]]

    return persons
