class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list) -> list:
    person_list = []
    person_list = [Person(person_dict["name"], person_dict["age"]) for person_dict in people_dicts]

    for person_dict in people_dicts:

        current_person_object = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            wife_name = person_dict["wife"]
            current_person_object.wife = Person.people[wife_name]

        elif person_dict.get("husband") is not None:
            husband_name = person_dict["husband"]
            current_person_object.husband = Person.people[husband_name]

    return person_list
