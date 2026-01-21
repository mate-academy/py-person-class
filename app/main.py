class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons = []

    for person_data in people:
        persons.append(Person(person_data.get("name"), person_data.get("age")))

    for person_data in people:
        person = Person.people.get(person_data.get("name"))
        if not person:
            continue

        if "wife" in person_data:
            if person_data.get("wife"):
                person.wife = Person.people.get(person_data.get("wife"))
            else:
                delattr(person, "wife")
        if "husband" in person_data:
            if person_data.get("husband"):
                person.husband = Person.people.get(person_data.get("husband"))
            else:
                delattr(person, "husband")

    return persons
