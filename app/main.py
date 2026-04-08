class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_people = [
        Person(
            name=person_data["name"], age=person_data["age"]
        ) for person_data in people
    ]
    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
    return list_people
