class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people[person_dict["husband"]]

    return list(Person.people.values())
