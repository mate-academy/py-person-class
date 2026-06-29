class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(p["name"], p["age"]) for p in people]

    for person_data in people:
        current = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name:
            current.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name:
            current.husband = Person.people[husband_name]

    return persons
