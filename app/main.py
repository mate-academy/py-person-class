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
    instances = [Person(person["name"], person["age"]) for person in people]

    for person_dict, instance in zip(people, instances):
        for key in ("wife", "husband"):
            if person_dict.get(key):
                setattr(instance, key, Person.people[person_dict[key]])

    return instances
