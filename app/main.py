class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person_data in people:
        Person(person_data["name"], person_data["age"])
    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people.get(person_data["wife"])
        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people.get(person_data["husband"])
    return list(Person.people.values())
