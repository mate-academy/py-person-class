class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    result = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            setattr(person_obj, "wife", Person.people[person_dict["wife"]])
        if person_dict.get("husband"):
            setattr(person_obj, "husband",
                    Person.people[person_dict["husband"]])

    return result
