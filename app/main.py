class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_dict = {}

    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        people_dict[name] = person_instance

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"] is not None:
            people_dict[name].wife = people_dict[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            people_dict[name].husband = people_dict[person["husband"]]

    return list(people_dict.values())
