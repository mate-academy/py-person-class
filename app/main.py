class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for entry in people:
        person = Person.people[entry["name"]]

        wife_name = entry.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
            if not hasattr(person.wife, "husband"):
                person.wife.husband = person

        husband_name = entry.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
            if not hasattr(person.husband, "wife"):
                person.husband.wife = person

    return person_list
