class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]

        if person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]
    return list(Person.people.values())
