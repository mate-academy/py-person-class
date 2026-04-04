class Person: people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]


    for person_dict, person_obj in zip(people, person_instances):
        for key in ("wife", "husband"):
            if key in person_dict and person_dict[key] is not None:
                partner_name = person_dict[key]
                setattr(person_obj, key, Person.people[partner_name])

    return person_instances
