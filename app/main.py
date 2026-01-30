class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(**person)
    person_class_list = [person for person in Person.people.values()]
    for person in people:
        if person.get("wife") or person.get("husband"):
            spouse_key = "wife"
            if person.get("husband"):
                spouse_key = "husband"

            person_instance = next(person_class_inst
                                   for person_class_inst in person_class_list
                                   if person_class_inst.name == person["name"])
            person_spouse = next(person_class_inst
                                 for person_class_inst in person_class_list
                                 if person_class_inst.name
                                 == person[spouse_key])

            setattr(person_instance, spouse_key, person_spouse)
    return person_class_list
