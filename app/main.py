class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    """
    This function takes list people
    and return list with Person instances instead of dicts.

    :param people: a list of dicts people, every dict means a person,
    it has keys: name, age, wife/husband - depends on person is male or female.
    All names are different.
    Key wife/husband can be either None or name of another person.
    :return: list with Person instances instead of dicts.
    """
    person_instances = []

    for person in people:
        name = person["name"]
        age = person["age"]
        person_instances.append(Person(name, age))

    husbands = [
        person for person in people
        if "wife" in person.keys()
        and person["wife"] is not None
    ]

    for husband in husbands:
        Person.people[husband["name"]].wife = Person.people[husband["wife"]]
        Person.people[husband["wife"]].husband = Person.people[husband["name"]]

    return person_instances
