class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_data: list) -> list:

    person_instances = [
        Person(p["name"], p["age"]) for p in people_data
    ]


    for p_dict in people_data:
        person_obj = Person.people[p_dict["name"]]

        for relation in ["wife", "husband"]:
            spouse_name = p_dict.get(relation)
            if spouse_name:
                setattr(person_obj, relation, Person.people[spouse_name])

    return person_instances