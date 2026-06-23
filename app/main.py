
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person.get("name"), person.get("age"))

    people_dict = Person.people

    for person in people:
        name = person.get("name")

        # wife
        if "wife" in person and person["wife"] is not None:
            people_dict[name].wife = people_dict[person.get("wife")]

        # husband
        if "husband" in person and person["husband"] is not None:
            people_dict[name].husband = people_dict[person.get("husband")]

    return list(people_dict.values())
