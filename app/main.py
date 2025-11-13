class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    instances = []
    for person_dict in people:
        inst = Person(person_dict["name"], person_dict["age"])
        instances.append(inst)

    for person_dict in people:
        inst = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            inst.wife = Person.people.get(person_dict["wife"])
        if "husband" in person_dict and person_dict["husband"] is not None:
            inst.husband = Person.people.get(person_dict["husband"])
    return instances
