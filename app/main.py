class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    res_person_instances = []
    for person in people:
        res_person_instances.append(Person(person["name"], person["age"]))

    for person in people:
        for key, value in person.items():
            if key == "wife" and value is not None:
                Person.people[person["name"]].wife = Person.people[value]
            elif key == "husband" and value is not None:
                Person.people[person["name"]].husband = Person.people[value]

    return res_person_instances
