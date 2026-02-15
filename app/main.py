class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(p["name"], p["age"]) for p in people]
    for i, person_dict in enumerate(people):
        inst = people_list[i]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name is not None:
            inst.wife = Person.people[wife_name]
        if husband_name is not None:
            inst.husband = Person.people[husband_name]
    return people_list
