class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    specimens_people = []

    for person in people:
        specimens_people.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        current_person = specimens_people[index]

        if "wife" in person and person["wife"] is not None:
            current_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            current_person.husband = Person.people[person["husband"]]

    return specimens_people
