class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    """
    Creates a list of Person objects based on a list of dictionaries.

    :param people: A list of dictionaries, where each dictionary
    represents a person with the following keys:
                   - "name" (str): The name of the person.
                   - "age" (int): The age of the person.
                   - "wife" (str | None): The name of the wife, if any.
                   - "husband" (str | None): The name of the husband, if any.
    :return: A list of Person objects, where each dictionary is converted
             into a corresponding Person object.
             If "wife" or "husband" is specified, links to the corresponding
             Person objects are established.
    """
    person_list = []
    # creating person instances and adding to person_list
    for person in people:
        person_list.append(Person(name=person["name"], age=person["age"]))
    # checking for the presence of the key wife or husband and if found,
    # assign the value wife or husband to the instance
    for person in people:
        current_person = Person.people[person["name"]]

        if wife_name := person.get("wife"):
            current_person.wife = Person.people[wife_name]

        if husband_name := person.get("husband"):
            current_person.husband = Person.people[husband_name]
    return person_list
