class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

        elif "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife \
                = Person.people[person["wife"]]

    return persons
