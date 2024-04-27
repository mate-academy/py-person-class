class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First, create all Person instances
    for person in people:
        Person(person["name"], person["age"])

    # Second, assign wife or husband if applicable
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]

    return list(Person.people.values())
