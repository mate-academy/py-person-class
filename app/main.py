class Person:
    people = {}  # Class attribute to store Person instances

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: dict) -> list:
    person_list = []
    for person_dict in people_dicts:
        name = person_dict["name"]
        age = person_dict["age"]
        person_list.append(Person(name, age))

    for person_dict in people_dicts:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if person_dict.get("wife"):
            spouse_name = person_dict["wife"]
            setattr(person_instance, "wife", Person.people[spouse_name])
        elif person_dict.get("husband"):
            spouse_name = person_dict["husband"]
            setattr(person_instance, "husband", Person.people[spouse_name])

    return person_list
