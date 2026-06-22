class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name, age)
        result.append(person_instance)

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            current_person.wife = Person.people[wife_name]
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            current_person.husband = Person.people[husband_name]
    return result
