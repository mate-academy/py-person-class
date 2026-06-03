class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people.clear()

    [Person(p_dict["name"], p_dict["age"]) for p_dict in people_dicts]

    result_list = []
    for p_dict in people_dicts:
        instance = Person.people[p_dict["name"]]

        if p_dict.get("wife") is not None:
            setattr(instance, "wife", Person.people[p_dict["wife"]])
        elif p_dict.get("husband") is not None:
            setattr(instance, "husband", Person.people[p_dict["husband"]])

        result_list.append(instance)

    return result_list
