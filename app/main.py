class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_instances = [
        Person(p_dict["name"], p_dict["age"])
        for p_dict in people
    ]

    for p_dict in people:
        name = p_dict["name"]
        current_person = Person.people[name]

        if p_dict.get("wife"):
            spouse_name = p_dict["wife"]
            current_person.wife = Person.people[spouse_name]
        elif p_dict.get("husband"):
            spouse_name = p_dict["husband"]
            current_person.husband = Person.people[spouse_name]

    return person_instances
