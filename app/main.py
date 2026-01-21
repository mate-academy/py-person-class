class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    persons = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                instance.wife = Person.people[wife_name]

        elif "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                instance.husband = Person.people[husband_name]

    return persons
