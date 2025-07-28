class Person:
    people = {} #dict

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(list_of_dicts: list) -> list:

    Person.people = {}

    for person_dict in list_of_dicts:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    result_list = []
    for person_dict in list_of_dicts:
        person_instance = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

        result_list.append(person_instance)

    return result_list
