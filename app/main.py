class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    result = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        result.append(person_instance)

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            wife_instance = Person.people[wife_name]
            person.wife = wife_instance

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            husband_instance = Person.people[husband_name]
            person.husband = husband_instance

    return result
