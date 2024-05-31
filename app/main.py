class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person_data["name"], person_data["age"]) for person_data in people]

    for person_data in people:
        if person_data.get("wife"):
            current_person = Person.people.get(person_data["name"])
            current_person.wife = Person.people.get(person_data["wife"])
        if person_data.get("husband"):
            current_person = Person.people.get(person_data["name"])
            current_person.husband = Person.people.get(person_data["husband"])
    return result
