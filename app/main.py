class Person:
    # Class attribute to store instances by their name
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Add instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Create instances of Person and store them in the list
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Set wife/husband attributes
    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            person_instance.husband = Person.people[person["husband"]]

    return person_list





