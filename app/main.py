class Person:
    # Class attribute to store Person instances by name
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person instance.

        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.name = name
        self.age = age
        # Add the instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    """
    Create a list of Person instances from a list of dictionaries.

    :param people: List of dictionaries containing person data.
    :return: List of Person instances.
    """
    # First, create Person instances without relationships
    person_instances = [
        Person(person["name"], person["age"])
        for person in people
    ]

    # Then, set relationships (wife/husband)
    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            instance.husband = Person.people[person["husband"]]

    return person_instances
