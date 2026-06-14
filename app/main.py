class Person:
    people = {}

def create_person_list(people_data):
    # First: create all Person instances
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])


def create_person_list(people: list) -> list:
    # First: create all Person instances
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])

    # Second: link wife/husband
    # Use Person.people.get() to find the spouse

    # Return list of Person instances
    return list(Person.people.values())
