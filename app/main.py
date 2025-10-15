class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_instances = []
    for person_data in people:
        instance = Person(person_data["name"], person_data["age"])
        person_instances.append(instance)

    for person_data, instance in zip(people, person_instances):
        if "wife" in person_data and person_data["wife"]:
            spouse_name = person_data["wife"]
            instance.wife = Person.people[spouse_name]
        elif "husband" in person_data and person_data["husband"]:
            spouse_name = person_data["husband"]
            instance.husband = Person.people[spouse_name]
    return person_instances
