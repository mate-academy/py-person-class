class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    # list comprehension
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        if person_data.get("wife") is not None:
            current_person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            current_person.husband = Person.people[person_data["husband"]]

    return person_list
