class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [(Person(person["name"], person["age"])) for person in people]

    for person_dict, person_obj in zip(people, result):
        wife_name = person_dict.get("wife")

        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")

        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return result
