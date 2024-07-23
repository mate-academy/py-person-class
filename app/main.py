class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    # Create all Person instances
    person_instances = [
        Person(person["name"], person["age"])
        for person in people_list
    ]
    for person_dict in people_list:
        person_instance = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            person_instance.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"]:
            person_instance.husband = Person.people[person_dict["husband"]]

    return person_instances
