class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for entry in people:
        person = Person.people[entry["name"]]
        spouse_name = entry.get("wife") or entry.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if entry.get("wife"):
                    person.wife = spouse
                else:
                    person.husband = spouse

    return person_list
