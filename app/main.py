class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for p_data, person in zip(people, person_list):
        if p_data.get("wife") is not None:
            person.wife = Person.people[p_data["wife"]]
        if p_data.get("husband") is not None:
            person.husband = Person.people[p_data["husband"]]

    return person_list
