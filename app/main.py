class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_person_instances = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        spouse = Person.people.get(person["name"])
        if "wife" in person and person["wife"]:
            spouse.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"]:
            spouse.husband = Person.people.get(person["husband"])

    return list_of_person_instances
