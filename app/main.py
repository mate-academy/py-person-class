class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for ind, person_data in enumerate(people):
        new_person = person_list[ind]
        if "wife" in person_data and person_data["wife"] is not None:
            new_person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"] is not None:
            new_person.husband = Person.people[person_data["husband"]]

    return person_list
