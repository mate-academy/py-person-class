class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(incoming_list: list) -> list:
    """

    :param incoming_list:
    :return:
    """
    persons_list = []
    for part_of_list in incoming_list:
        name = part_of_list["name"]
        age = part_of_list["age"]
        person = Person(name, age)
        persons_list.append(person)
    for i, part_of_list in enumerate(incoming_list):
        if part_of_list.get("wife"):
            persons_list[i].wife = \
                Person.people[part_of_list.get("wife")]
        if part_of_list.get("husband"):
            persons_list[i].husband = \
                Person.people[part_of_list.get("husband")]
    return persons_list
