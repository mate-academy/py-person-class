class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict, person_instance in zip(people, person_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

    return person_list
