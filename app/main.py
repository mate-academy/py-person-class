class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    Person.people.clear()

    for person_dict in people_dicts:
        Person(name=person_dict["name"], age=person_dict["age"])

    result_list = []
    for person_dict in people_dicts:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

        result_list.append(person_instance)

    return result_list
