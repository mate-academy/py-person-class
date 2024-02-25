class Person:

    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list:
    """
    this function takes list people and return
    list with Person instances instead of dicts.
    """

    people_result = [
        Person(name=person_dict["name"], age=person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person_name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            Person.people[person_name].wife = Person.people[wife_name]
            Person.people[wife_name].husband = Person.people[person_name]
    return people_result
