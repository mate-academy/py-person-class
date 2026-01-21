class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        people_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return people_list
