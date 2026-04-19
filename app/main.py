class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        for key, value in person.items():
            if key == "wife" and value is not None:
                person_obj = Person.people[person["name"]]
                person_obj.wife = Person.people[value]
            elif key == "husband" and value is not None:
                person_obj = Person.people[person["name"]]
                person_obj.husband = Person.people[value]

    return person_list
