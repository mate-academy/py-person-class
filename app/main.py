class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people = {}
    [Person(p["name"], p["age"]) for p in people_dicts]

    for p_dict in people_dicts:
        person_instance = Person.people[p_dict["name"]]
        wife_name = p_dict.get("wife")
        husband_name = p_dict.get("husband")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]
    return list(Person.people.values())
