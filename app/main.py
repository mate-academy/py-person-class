class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    instances = [Person(person["name"], person["age"]) for person in people]
    for person, inst in zip(people, instances):
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            inst.wife = Person.people[wife_name]
        if husband_name is not None:
            inst.husband = Person.people[husband_name]
    return instances
