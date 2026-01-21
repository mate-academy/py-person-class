class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        instance_person = Person(person["name"], person["age"])
        result.append(instance_person)
    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            current_person = Person.people[person["name"]]
            spouse = Person.people[person["wife"]]
            current_person.wife = spouse
        elif "husband" in person.keys() and person["husband"] is not None:
            current_person = Person.people[person["name"]]
            spouse = Person.people[person["husband"]]
            current_person.husband = spouse
    return result
