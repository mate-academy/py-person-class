class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> None:
    person_list = []
    for person in people:
        person_instance = Person(name=person["name"], age=person["age"])
        person_list.append(person_instance)

    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_instance.husband = Person.people[person["husband"]]

    return person_list
