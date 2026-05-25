class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for i, person_dict in enumerate(people):
        person_obj = person_list[i]

        wife_name = person_dict.get("wife")
        if wife_name and wife_name in Person.people:
            person_obj.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name and husband_name in Person.people:
            person_obj.husband = Person.people[husband_name]

    return person_list
