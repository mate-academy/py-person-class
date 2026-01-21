class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"]:
            person_instance.husband = Person.people.get(person["husband"])

    return person_list
