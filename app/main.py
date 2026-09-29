class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(p["name"], p["age"]) for p in people]

    for person_dict, person_instance in zip(people, person_instances):
        if person_dict.get("wife"):
            wife_name = person_dict.get("wife")
            person_instance.wife = Person.people[wife_name]
        elif person_dict.get("husband"):
            husband_name = person_dict.get("husband")
            person_instance.husband = Person.people[husband_name]

    return person_instances
