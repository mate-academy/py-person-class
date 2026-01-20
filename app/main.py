class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    [Person(p["name"], p["age"]) for p in people]

    for person in people:
        current_person = Person.people[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            current_person.wife = Person.people[person["wife"]]
        elif husband_name is not None:
            current_person.husband = Person.people[person["husband"]]
    return list(Person.people.values())
