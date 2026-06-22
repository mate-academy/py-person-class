class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for i, person_dict in enumerate(people):
        person_obj = result[i]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return result
