class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    # complete the dict for it be non empty
    for person in people:
        Person(person["name"], person["age"])

    # run throw the list and set the "husband" and "wife"
    for person in people:
        current_name = Person.people.get(person.get("name"))
        if "wife" in person and person["wife"] is not None:
            current_name.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"] is not None:
            current_name.husband = Person.people.get(person["husband"])

    return [pers for pers in Person.people.values()]
