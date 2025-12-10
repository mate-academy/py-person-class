class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    for person_data in people:
        new_person = Person(person_data["name"], person_data["age"])
        if "wife" in person_data and person_data["wife"]:
            new_person.wife = person_data["wife"]
        if "husband" in person_data and person_data["husband"]:
            new_person.husband = person_data["husband"]

    person_list_result = []

    for person in Person.people.values():
        if person.wife:
            person.wife = Person.people.get(person.wife)
        else:
            del person.wife

        if person.husband:
            person.husband = Person.people.get(person.husband)
        else:
            del person.husband

        person_list_result.append(person)

    return person_list_result
