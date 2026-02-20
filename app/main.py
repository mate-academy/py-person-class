class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people_list: list[dict[str, object]],
) -> list[Person]:
    instances: list[Person] = []

    for person_dict in people_list:
        person = Person(person_dict["name"], person_dict["age"])
        instances.append(person)

    for person_dict, person_obj in zip(people_list, instances):
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return instances
