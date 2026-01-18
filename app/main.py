
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def set_wife(self, wife: dict) -> None:
        """add wife"""
        self.wife = wife
        wife.husband = self

    def set_husband(self, husband: dict) -> None:
        """add husband"""
        self.husband = husband
        husband.wife = self


def create_person_list(person_data: list) -> list:
    """Creates a list of all dictionary elements"""
    persons = {
        data["name"]: Person(data["name"], data["age"]) for data in person_data
    }

    for data in person_data:
        person = persons[data["name"]]

    wife = persons.get(data.get("wife"))
    husband = persons.get(data.get("husband"))

    wife and person.set_wife(wife)
    husband and person.set_husband(husband)

    return list(persons.values())
