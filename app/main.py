class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list) -> list:
    """
    Creates Person instances from a list of dictionaries and then links
    them using spouse references. All Person objects are created first
    using a list comprehension, which automatically populates the
    Person.people registry. After that, spouse relationships ("wife" or
    "husband") are established by looking up corresponding Person
    instances in the shared registry.

    :param people_list: list of dictionaries describing people. Each dict
     must contain "name" and "age", and may optionally contain "wife"
     or "husband" mapped to another persons name.
    :return: list of Person instances with spouse attributes assigned
     where such relationships are defined
    """
    list_with_people = [
        Person(person.get("name"), person.get("age")) for person in people_list
    ]

    for person in people_list:
        current_person = Person.people.get(person.get("name"))

        if person.get("wife"):
            current_person.wife = Person.people.get(person.get("wife"))

        if person.get("husband"):
            current_person.husband = Person.people.get(person.get("husband"))

    return list_with_people
