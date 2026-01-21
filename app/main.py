
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    final_list = []
    for person in people:
        final_list.append(Person(person["name"], person["age"]))
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]
    return final_list
