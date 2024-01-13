class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for human in people_list:
        if "wife" in human.keys():
            if human["wife"] is not None:

                way_to_human = Person.people[human["name"]]
                way_to_human.wife = Person.people[human["wife"]]
        if "husband" in human.keys():
            if human["husband"] is not None:

                way_to_human = Person.people[human["name"]]
                way_to_human.husband = Person.people[human["husband"]]
    return person_instances
