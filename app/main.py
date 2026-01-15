class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    instances_list = [Person(dct["name"], dct["age"]) for dct in people]

    for dct, instance in zip(people, instances_list):
        if dct.get("wife"):
            instance.wife = Person.people[dct["wife"]]
        if dct.get("husband"):
            instance.husband = Person.people[dct["husband"]]
    return instances_list
