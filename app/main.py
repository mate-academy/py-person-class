class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: list) -> list:
    person_instances = [
        Person(name=p["name"], age=p["age"]) for p in people_data
    ]

    for person_dict in people_data:
        if person_dict.get("wife"):
            person_object = Person.people[person_dict["name"]]
            wife_object = Person.people[person_dict["wife"]]
            person_object.wife = wife_object
        elif person_dict.get("husband"):
            person_object = Person.people[person_dict["name"]]
            husband_object = Person.people[person_dict["husband"]]
            person_object.husband = husband_object

    return person_instances
