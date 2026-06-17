class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_instances = [
        Person(p["name"], p["age"]) for p in people
    ]
    for person_dict in people:
        current_name = person_dict["name"]
        current_instance = Person.people[current_name]
        if person_dict.get("wife") is not None:
            wife_name = person_dict["wife"]
            current_instance.wife = Person.people[wife_name]
        elif person_dict.get("husband") is not None:
            husband_name = person_dict["husband"]
            current_instance.husband = Person.people[husband_name]
    return person_instances
