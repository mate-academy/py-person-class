class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        new_people_list.append(new_person)

    for partner in new_people_list:
        for person in people:
            if partner.name == person["name"]:
                if "wife" in person and person["wife"] is not None:
                    partner.wife = Person.people[person["wife"]]
                if "husband" in person and person["husband"] is not None:
                    partner.husband = Person.people[person["husband"]]

    return new_people_list
