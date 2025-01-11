class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for i, person_info in enumerate(people):
        if person_info.get("wife") is not None:
            persons[i].wife = Person.people[person_info["wife"]]
        elif person_info.get("husband") is not None:
            persons[i].husband = Person.people[person_info["husband"]]
    return persons
