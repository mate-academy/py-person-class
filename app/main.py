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

        if person.get("wife"):
            new_person.wife = person["wife"]
        elif person.get("husband"):
            new_person.husband = person["husband"]

        persons.append(new_person)

    for person in persons:
        if "wife" in person.__dict__:
            person.wife = Person.people[person.wife]
        elif "husband" in person.__dict__:
            person.husband = Person.people[person.husband]

    return persons
