class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            new_person.wife = person["wife"]

        if "husband" in person and person["husband"] is not None:
            new_person.husband = person["husband"]

        new_people_list.append(new_person)

    return new_people_list
