class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for p_dict in people:
        person = Person(p_dict["name"], p_dict["age"])
        person_instances.append(person)
    for p_dict in people:
        current_person = Person.people[p_dict["name"]]
        if "wife" in p_dict and p_dict["wife"] is not None:
            wife_name = p_dict["wife"]
            if wife_name in Person.people:
                current_person.wife = Person.people[wife_name]
        elif "husband" in p_dict and p_dict["husband"] is not None:
            husband_name = p_dict["husband"]
            if husband_name in Person.people:
                current_person.husband = Person.people[husband_name]
    return person_instances
