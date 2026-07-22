class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, p_dict: dict) -> None:
        if p_dict.get("wife"):
            self.wife = Person.people[p_dict["wife"]]
        elif p_dict.get("husband"):
            self.husband = Person.people[p_dict["husband"]]


def create_person_list(people_data: list) -> list:
    Person.people = {}

    person_list = [
        Person(p_dict["name"], p_dict["age"])
        for p_dict in people_data
    ]

    [
        Person.people[p_dict["name"]].set_spouse(p_dict)
        for p_dict in people_data
    ]

    return person_list