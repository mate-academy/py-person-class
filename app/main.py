class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        # Initialize the name and age of the person and add the instance to
        # the people dictionary
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    """
    Creates a list of Person instances from a list of dictionaries
    containing person information.

    Args:
        people (list): A list of dictionaries, where each dictionary contains
        the keys "name", "age", and optionally "wife" or "husband".
    Returns:
        list: A list of Person instances created from the input data.
    """

    # Clear the people dictionary to avoid conflicts with previous instances
    Person.people.clear()

    # Create all instances of Person
    for person in people:
        Person(name=person["name"], age=person["age"])

    # Assign the relationships of wife/husband
    for person in people:
        instance: Person = Person.people[person["name"]]

        if person.get("wife"):
            instance.wife = Person.people[person["wife"]]

        if person.get("husband"):
            instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
