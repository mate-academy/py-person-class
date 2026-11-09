class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data, person in zip(people, person_list):
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return person_list
