class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    instances_list = []

    for person in people:
        new_instance = Person(name=person["name"], age=person["age"])
        instances_list.append(
            new_instance
        )
        if person.get("wife"):
            new_instance.wife = person["wife"]

    for instance in instances_list:
        if hasattr(instance, "wife"):
            wife = Person.people.get(instance.wife)
            husband = instance
            husband.wife, wife.husband = wife, husband

    return instances_list
