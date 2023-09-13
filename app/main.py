class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]

    return people_instances
