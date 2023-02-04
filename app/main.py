class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    list_person = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        list_person.append(person_instance)
        Person.people[person_instance.name] = person_instance

    add_wife(people, list_person)
    add_husband(people, list_person)
    return list_person


def add_wife(people: list, list_person: list) -> None:
    for person in people:
        if "wife" in person and person["wife"] is not None:
            for husband in list_person:
                for wife in list_person:
                    if (
                        person["wife"] == wife.name
                        and person["name"] == husband.name
                    ):
                        husband.wife = wife


def add_husband(people: list, list_person: list) -> None:
    for person in people:
        if "husband" in person and person["husband"] is not None:
            for wife in list_person:
                for husband in list_person:
                    if (
                        person["husband"] == husband.name
                        and person["name"] == wife.name
                    ):
                        wife.husband = husband
