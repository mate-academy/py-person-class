class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        person_instance = Person(
            name=person_dict["name"],
            age=person_dict["age"]
        )
        person_list.append(person_instance)

    for person_dict, person_instance in zip(people, person_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

    return person_list
