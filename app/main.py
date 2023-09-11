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
        if person_dict.get("wife"):
            Person.people[person_dict["name"]].wife = \
                Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            Person.people[person_dict["name"]].husband = \
                Person.people[person_dict["husband"]]

    return people_instances
