class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    person_instances = [
        Person(name=p["name"], age=p["age"])
        for p in people
    ]

    for p_dict in people:
        person_obj = Person.people[p_dict["name"]]

        if p_dict.get("wife") is not None:
            person_obj.wife = Person.people[p_dict["wife"]]
        elif p_dict.get("husband") is not None:
            person_obj.husband = Person.people[p_dict["husband"]]

    return person_instances
