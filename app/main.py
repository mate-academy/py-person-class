class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_insts = []
    for person in people:
        person_obj = Person(person["name"], person["age"])
        if person.get("wife", None) or person.get("husband", None):
            for person_inst in person_insts:
                if person_inst.name == person.get("wife", None):
                    person_obj.wife = person_inst
                    person_inst.husband = person_obj
                elif person_inst.name == person.get("husband", None):
                    person_obj.husband = person_inst
                    person_inst.wife = person_obj
        person_insts.append(person_obj)
    Person.people.update({person_obj: person_inst})
    return person_insts
