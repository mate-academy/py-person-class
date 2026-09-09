class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for p_dict in people:
        person_obj = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            wife_name = p_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        elif p_dict.get("husband"):
            husband_name = p_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return person_list
