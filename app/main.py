class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for name in people:
        person_obj = Person.people[name["name"]]
        if "wife" in name and not name["wife"] is None:
            person_obj.wife = Person.people[name["wife"]]
        elif "husband" in name and not name["husband"] is None:
            person_obj.husband = Person.people[name["husband"]]
    return person_lis
