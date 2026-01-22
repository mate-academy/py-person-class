class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person.wife = Person.people.get(person_dict["wife"])
        if person_dict.get("husband"):
            person.husband = Person.people.get(person_dict["husband"])
    return person_instances
