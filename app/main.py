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

    for index, partner in enumerate(new_people_list):
        if partner.name == people[index]["name"]:
            if "wife" in people[index] and people[index]["wife"] is not None:
                partner.wife = Person.people[people[index]["wife"]]
            if "husband" in people[index] and people[index]["husband"] is not None:
                partner.husband = Person.people[people[index]["husband"]]

    return new_people_list
