class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    # add people to list
    for dict_of_person in people:
        new_person = Person(dict_of_person["name"], dict_of_person["age"])
        person_list.append(new_person)
    # add attributes to each person
    class_list = Person.people
    for person in people:
        if "wife" in person and person["wife"] is not None:
            class_list[person["name"]].wife = class_list[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            class_list[person["name"]].husband = class_list[person["husband"]]
    return person_list
