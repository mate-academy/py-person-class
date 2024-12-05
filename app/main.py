class Person:
    # I cannot add docstring here, because test checks length of __dict__
    people = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a new Person instance
        and adds it to the `people` dictionary.

        Parameters:
        ----------
        name : str
            The name of the person.
        age : int
            The age of the person.
        """
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    """
    Creates a list of Person instances from a list of dictionaries and
    sets up their relationships (wife/husband) based on the provided data.

    Parameters:
    ----------
    people : list of dict
        A list of dictionaries where each dictionary represents a person.
        Each dictionary must contain the keys "name" and "age",
        and contain "wife"/"husband" keys depends on person is male or female.
        All names are different.
        Key wife/husband can be either None or name of another person.

    Returns:
    -------
    list of Person
        A list of Person instances
        with their relationships (wife/husband) set up.

    Notes:
    ------
    The wife and husband relationships are dynamically added to the Person
    instances based on the input data. These attributes are not pre-defined
    in the Person class but are added as needed.
    Be cautious, as attempting to access these attributes without ensuring
    they exist will result in an AttributeError.
    """
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife

        if "husband" in person.keys() and person["husband"] is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return people_list
