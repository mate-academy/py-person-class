class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def display(self: "Person") -> None:
        print(self.name)
        print(self.age)


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        instances.append(Person(person["name"], person["age"]))

    for person_dict, instance in zip(people, instances):
        for key in ("wife", "husband"):
            if key in person_dict and person_dict[key] is not None:
                setattr(instance, key, Person.people[person_dict[key]])

    return instances
