class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    person_instances = [
        Person(person_data.get("name"), person_data.get("age"))
        for person_data in people
    ]

    for person_data, instance in zip(people, person_instances):
        spouse_name = person_data.get("wife")
        if spouse_name:
            instance.wife = Person.people[spouse_name]
        spouse_name = person_data.get("husband")
        if spouse_name:
            instance.husband = Person.people[spouse_name]

    return person_instances
