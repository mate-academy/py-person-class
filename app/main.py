class Person:
    people = {}

    def __init__(self, name: str, age: int, *args, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_instances = [Person(**person) for person in people]
    for person_data, person_instance in zip(people, person_instances):
        if person_data.get("wife"):
            person_instance.wife = Person.people.get(person_data["wife"])
        elif person_data.get("husband"):
            person_instance.husband = Person.people.get(person_data["husband"])
    return person_instances
