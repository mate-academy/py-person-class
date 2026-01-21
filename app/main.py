class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        if person["name"] not in Person.people:
            Person(person["name"], person["age"])
    for person in people:
        person_instance = Person.people[person["name"]]
        if "husband" in person and person["husband"] is not None:
            person_instance.husband = Person.people.get(person["husband"])
        elif "wife" in person and person["wife"] is not None:
            person_instance.wife = Person.people.get(person["wife"])
    return list(Person.people.values())
