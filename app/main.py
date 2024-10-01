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
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people.get(person_dict["wife"], None)
        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"], None)
    return person_instances
