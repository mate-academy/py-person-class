class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:

    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people.get(person["name"])
        if person.get("wife"):
            person_instance.wife = Person.people.get(person.get("wife"))
        if person.get("husband"):
            person_instance.husband = Person.people.get(person.get("husband"))

    return people_list
