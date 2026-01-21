class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person in people:

        if person.get("wife"):
            Person.people[person.get("name")].wife = (
                Person.people.get(person.get("wife"))
            )

        if person.get("husband"):
            Person.people[person.get("name")].husband = (
                Person.people.get(person.get("husband"))
            )

    return person_list
