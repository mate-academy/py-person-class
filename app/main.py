class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    Person.people = {}

    persons = [Person(pd["name"], pd["age"]) for pd in people_dicts]

    for pd in people_dicts:
        p1 = Person.people[pd["name"]]
        if pd.get("wife"):
            p1.wife = Person.people[pd["wife"]]
        if pd.get("husband"):
            p1.husband = Person.people[pd["husband"]]

    return persons
