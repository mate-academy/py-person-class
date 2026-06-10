class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_obj = Person.people[person.get("name")]
        if "wife" in person and person.get("wife") is not None:
            person_obj.wife = Person.people[person.get("wife")]
        if "husband" in person and person.get("husband") is not None:
            person_obj.husband = Person.people[person.get("husband")]

    return person_list
