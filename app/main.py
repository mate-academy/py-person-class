class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    [Person(p_dict["name"], p_dict["age"]) for p_dict in people]

    for p_dict in people:
        person = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            person.wife = Person.people[p_dict["wife"]]

        if p_dict.get("husband"):
            person.husband = Person.people[p_dict["husband"]]

    return [Person.people[p_dict["name"]] for p_dict in people]
