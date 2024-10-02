class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            person_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
