class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"] is not None:
                wife = Person.people[person["wife"]]
                current_person.wife = wife
        if "husband" in person:
            if person["husband"] is not None:
                husband = Person.people[person["husband"]]
                current_person.husband = husband
    return result
