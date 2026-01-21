class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    obj_list = []
    for info in people:
        person_obj = Person(info["name"], info["age"])
        obj_list.append(person_obj)

    for info in people:
        person_obj = Person.people[info["name"]]
        if "wife" in info and info["wife"] is not None:
            person_obj.wife = Person.people[info["wife"]]
        if "husband" in info and info["husband"] is not None:
            person_obj.husband = Person.people[info["husband"]]
    return obj_list
