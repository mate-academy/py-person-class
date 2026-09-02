class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person in people:
        new_person = Person(person["name"], person["age"])

        if person.get("wife") is not None:
            new_person.wife = person["wife"]

        if person.get("husband") is not None:
            new_person.husband = person["husband"]

        persons.append(new_person)

    for person in persons:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]

        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return persons
