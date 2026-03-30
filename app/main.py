class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people = {}
    instances = [Person(p["name"], p["age"]) for p in people_dicts]
    for p_dict in people_dicts:
        current_person = Person.people[p_dict["name"]]
        for key in ["wife", "husband"]:
            spouse_name = p_dict.get(key)
            if spouse_name:
                spouse_instance = Person.people[spouse_name]
                setattr(current_person, key, spouse_instance)
    return instances
