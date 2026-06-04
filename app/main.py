class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people):
    Person.people = {}

    persons = []

    # Create all Person objects
    for person_data in people:
        person = Person(
            person_data["name"],
            person_data["age"]
        )
        persons.append(person)

    # Create wife/husband links
    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    return persons
