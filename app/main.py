class Person:
    people = {}  # Create a dictionary to store all instances

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.husband = None
        self.wife = None
        # Add an instance to the dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        # Add instance people to the Person.people
        Person(name=person["name"], age=person["age"])

    for i in people:
        person = Person.people[i["name"]]  # Get the object of the current person

        if "husband" in i and i["husband"]:
            person.husband = Person.people[i["husband"]]
        if "wife" in i and i["wife"]:
            person.wife = Person.people[i["wife"]]

        # Remove husband/wife if they are still None
        if person.husband is None:
            del person.husband
        if person.wife is None:
            del person.wife

    # Return the list of created Person instances
    return list(Person.people.values())
