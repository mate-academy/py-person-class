class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    Person.people = {}

    person_instances = [Person(p["name"], p["age"]) for p in people_dicts]

    for person_dict in people_dicts:
        current_person_name = person_dict["name"]
        current_person_obj = Person.people[current_person_name]

        wife_name = person_dict.get("wife")
        wife_object = Person.people.get(wife_name)
        if wife_object:
            current_person_obj.wife = wife_object
        elif wife_name is not None:
            print(f"Warning: Wife \"{wife_name}\" not found for "
                  f"\"{current_person_obj.name}\".")

        husband_name = person_dict.get("husband")
        husband_object = Person.people.get(husband_name)
        if husband_object:
            current_person_obj.husband = husband_object
        elif husband_name is not None:
            print(f"Warning: Husband \"{husband_name}\" not found for "
                  f"\"{current_person_obj.name}\".")

    return person_instances
