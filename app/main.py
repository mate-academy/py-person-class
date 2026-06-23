
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person["name"], person["age"])

    people_dict = Person.people

    for person in people:
        name = person.get("name")

        # wife
        wife = person.get("wife", None)
        if wife is not None:
            people_dict[name].wife = people_dict[wife]

        # husband
        husband = person.get("husband", None)
        if husband is not None:
            people_dict[name].husband = people_dict[husband]

    return list(people_dict.values())
