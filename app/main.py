class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    name_to_person = {}
    person_instances = [
        Person(person["name"], person["age"]) for person in people_data
    ]
    for person_instance in person_instances:
        name_to_person[person_instance.name] = person_instance
    for person in people_data:
        person_instance = name_to_person[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            person_instance.wife = name_to_person[wife_name]
        if husband_name is not None:
            person_instance.husband = name_to_person[husband_name]

    return person_instances
