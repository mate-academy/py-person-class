class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people.update({f"{name}": self})


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))
    for position, person in enumerate(people):
        people_dict = Person.people
        if "wife" in person:
            if person["wife"] is not None:
                person_list[position].wife = people_dict[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                person_list[position].husband = people_dict[person["husband"]]
    return person_list
