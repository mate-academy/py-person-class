class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        obj = Person(person_dict["name"], int(person_dict["age"]))
        person_list.append(obj)

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_obj = Person.people[person_dict["wife"]]
            person.wife = wife_obj

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_obj = Person.people[person_dict["husband"]]
            person.husband = husband_obj

    return person_list
