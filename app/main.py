class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in people:
        new_person = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            new_person.wife = Person.people[person["wife"]]
            new_person.wife.husband = new_person

    return person_list
