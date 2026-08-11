class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(p["name"], p["age"]) for p in people]

    for person_dict, person_obj in zip(people, person_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return person_list
