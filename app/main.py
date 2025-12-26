class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # 1. Create all Person instances (list comprehension)
    persons = [Person(p["name"], p["age"]) for p in people]

    # 2. Link spouses AFTER all objects exist
    for p in people:
        person = Person.people[p["name"]]

        wife_name = p.get("wife")
        husband_name = p.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)

        if husband_name:
            person.husband = Person.people.get(husband_name)

    return persons