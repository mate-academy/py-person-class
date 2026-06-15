class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        if person.get("wife") or person.get("husband"):
            if person.get("wife"):
                key = "wife"
            else:
                key = "husband"
            setattr(Person.people[person["name"]], key,
                    Person.people[person[key]])
    return person_list
