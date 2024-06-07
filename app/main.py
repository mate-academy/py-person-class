class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    add_person(people_list)
    set_spouses(people_list)
    return list(Person.people.values())


def add_person(people_list: list[dict]) -> None:
    for person in people_list:
        name = person["name"]
        age = person["age"]
        Person(name, age)


def set_spouses(people_list: list[dict]) -> None:
    for person in people_list:
        name = person["name"]
        if "wife" in person and person["wife"]:
            Person.people[name].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            Person.people[name].husband = Person.people[person["husband"]]
