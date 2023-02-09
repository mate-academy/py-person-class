class Person:
    people = {}

    def __init__(self, name: str, age: str) -> any:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        Person(person["name"], person["age"])
        person_list.append(Person.people[person["name"]])
    pers_dict = Person.people
    for person in people:
        if "wife" in person and person["wife"] is not None:
            pers_dict[person["name"]].wife = pers_dict[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            pers_dict[person["name"]].husband = pers_dict[person["husband"]]

    return person_list
