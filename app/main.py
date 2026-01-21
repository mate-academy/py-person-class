class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes an instance of the Person class and registers the
        instance in the class-level dictionary using the name as the key.
        This constructor assigns the provided name and age to the
        instance attributes.

        :param name: The name of the person.
        :type name: str
        :param age: The age of the person.
        :type age: int
        """
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    """
    Creates a list of `Person` objects based on the provided list of
    dictionaries, assigning relationships (wife or husband) if such
    attributes are specified in the input data.

    :param people: A list of dictionaries where each dictionary
                   represents a person with their attributes
                   such as name, age, and optionally
                   spouse information (wife or husband).
    :type people: list
    :return: A list of `Person` instances created from the input data.
    :rtype: list
    """
    person_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person, person_dict in zip(person_instances, people):
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_instances
