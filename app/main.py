class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person = Person(person["name"], person["age"])
        person_list.append(person)

    for person in people:
        if ("wife" in person and person["wife"] is not None) or (
                "husband" in person and person["husband"] is not None
        ):
            if "wife" in person:
                key = "wife"
            else:
                key = "husband"
            setattr(Person.people[person["name"]], key,
                    Person.people[person[key]])
    return person_list
