class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        __class__.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))

    cls_dict = Person.people

    for person in people:
        if "wife" in person and person["wife"] is not None:
            cls_dict[person["name"]].wife = cls_dict[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            cls_dict[person["name"]].husband = cls_dict[person["husband"]]

    return people_list
