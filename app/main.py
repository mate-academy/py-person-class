class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list[dict]) -> list:
    person_list = [
        Person(person["name"], person["age"]) for person in people_list
    ]

    for person in people_list:
        person_obj = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            person_obj.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            person_obj.husband = Person.people[person["husband"]]

    return person_list
