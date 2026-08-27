class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for p_dict in people:
        person_instance = Person.people[p_dict["name"]]
        spouse_key = "wife" if "wife" in p_dict else "husband"
        spouse_name = p_dict.get(spouse_key)

        if spouse_name is not None:
            setattr(person_instance, spouse_key, Person.people[spouse_name])

    return person_list
