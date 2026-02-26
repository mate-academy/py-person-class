class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list[dict]) -> list:
    objects_list = [
        Person(individual.get("name"), individual.get("age"))
        for individual in people_list
    ]

    for i, individual in enumerate(people_list):
        partner = individual.get("wife")
        if partner:
            objects_list[i].wife = Person.people.get(partner)
        partner = individual.get("husband")
        if partner:
            objects_list[i].husband = Person.people.get(partner)

    return objects_list
