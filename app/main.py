class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people_list
    ]

    for human in people_list:
        if human.get("wife") is not None:
            way_to_instance = Person.people[human["name"]]
            way_to_instance.wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            way_to_instance = Person.people[human["name"]]
            way_to_instance.husband = Person.people[human["husband"]]
    return person_instances
