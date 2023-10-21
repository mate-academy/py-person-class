class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i, person in enumerate(people):
        if "wife" in person and person.get("wife") is not None:
            person_list[i].wife = Person.people[person["wife"]]
        elif "husband" in person and person.get("husband") is not None:
            person_list[i].husband = Person.people[person["husband"]]
    return person_list
