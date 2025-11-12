class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(d["name"], d["age"]) for d in people]
    for person_dict in people:
        owner = Person.people[person_dict["name"]]
        if person_dict.get("wife") is not None:
            partner = Person.people[person_dict["wife"]]
            owner.wife = partner
        if person_dict.get("husband") is not None:
            partner = Person.people[person_dict["husband"]]
            owner.husband = partner
    return person_list
