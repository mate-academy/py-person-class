class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(p["name"], p["age"]) for p in people]
    for p_dict in people:
        current_person = Person.people[p_dict["name"]]
        wife_name = p_dict.get("wife")
        if wife_name:
            current_person.wife = Person.people[wife_name]
        husband_name = p_dict.get("husband")
        if husband_name:
            current_person.husband = Person.people[husband_name]
    return person_instances
