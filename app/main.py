class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = [
        Person(person["name"], person["age"])
        for person in people_list
    ]
    for person_dict in people_list:
        person_instance = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person_instance.wife = Person.people[wife_name]
        if husband_name:
            person_instance.husband = Person.people[husband_name]

    return person_instances
