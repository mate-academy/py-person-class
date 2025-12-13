class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_inst = [Person(p_dict["name"], p_dict["age"]) for p_dict in people]
    for p_dict in people:
        current_person = Person.people[p_dict["name"]]
        wife_name = p_dict.get("wife")
        husband_name = p_dict.get("husband")
        if wife_name and wife_name in Person.people:
            current_person.wife = Person.people[wife_name]
        elif husband_name and husband_name in Person.people:
            current_person.husband = Person.people[husband_name]
    return person_inst
