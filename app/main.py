class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts):
    person_list = [
        Person(p["name"], p["age"])
        for p in people_dicts
    ]

    for p_dict in people_dicts:
        person = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            person.wife = Person.people[p_dict["wife"]]

        if p_dict.get("husband"):
            person.husband = Person.people[p_dict["husband"]]

    return person_list
