class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(person_dict["name"], person_dict["age"]) for person_dict in people]
    [setattr(person_instances[[person_dict["name"] for person_dict in people].index(person_dict["name"])], "husband",
             person_instances[
                 [person_dict["name"] for person_dict in people].index(person_dict.get("husband"))]) if person_dict.get(
        "husband") else None for person_dict in people]
    [setattr(person_instances[[person_dict["name"] for person_dict in people].index(person_dict["name"])], "wife",
             person_instances[
                 [person_dict["name"] for person_dict in people].index(person_dict.get("wife"))]) if person_dict.get(
        "wife") else None for person_dict in people]
    return person_instances
