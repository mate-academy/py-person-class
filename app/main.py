class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        instances.append(Person(person["name"], person["age"]))
    for index_1, person in enumerate(people):
        for index_2, check in enumerate(people):
            if person.get("wife") == check["name"]:
                instances[index_1].wife = instances[index_2]
            if person.get("husband") == check["name"]:
                instances[index_1].husband = instances[index_2]
    return instances
