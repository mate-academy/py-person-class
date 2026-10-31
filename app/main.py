class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people_data]

    for person_dict, person_instance in zip(people_data, person_list):
        if wife_name := person_dict.get("wife"):
            person_instance.wife = Person.people[wife_name]
        elif husband_name := person_dict.get("husband"):
            person_instance.husband = Person.people[husband_name]

    return person_list
