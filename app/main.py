class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict.get("name"), person_dict.get("age"))
        for person_dict in people
        if isinstance(person_dict.get("name"), str)
        and isinstance(person_dict.get("age"), int)
    ]
    for person_dict in people:
        current_name = person_dict.get("name")
        current_person_obj = Person.people.get(current_name)
        if current_person_obj is None:
            continue

        relation_key = None
        linked_name = None
        wife_name = person_dict.get("wife")

        if isinstance(wife_name, str):
            relation_key = "wife"
            linked_name = wife_name

        elif isinstance(person_dict.get("husband"), str):
            relation_key = "husband"
            linked_name = person_dict.get("husband")
        else:
            continue

        if linked_name in Person.people:
            linked_person_obj = Person.people[linked_name]
            setattr(current_person_obj, relation_key, linked_person_obj)
    return person_list
