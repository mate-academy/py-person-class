class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
    for person in people:
        if "wife" in person and person["wife"] is not None:
            current_person = Person.people[person["name"]]
            current_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            current_person = Person.people[person["name"]]
            current_person.husband = Person.people[person["husband"]]
    return person_list
